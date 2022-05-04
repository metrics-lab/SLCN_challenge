# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2022-04-20 10:10:19
# @Last Modified by:   Your name
# @Last Modified time: 2022-05-04 10:38:36

from typing import Dict

import SimpleITK
import numpy as np

from evalutils import ClassificationAlgorithm
from evalutils.validators import (
    UniquePathIndicesValidator,
    UniqueImagesValidator,
)

#### Import librairies requiered for your model and predictions
import torch
from model.sit import SiT
import pandas as pd
from pathlib import Path
import json
from glob import glob

execute_in_docker = True

class Slcn_algorithm(ClassificationAlgorithm):
    def __init__(self):
        super().__init__(
            validators=dict(
                input_image=(
                    UniqueImagesValidator(),
                    UniquePathIndicesValidator(),
                )
            ),
            input_path = Path("/input/images/cortical-surface-mesh/") if execute_in_docker else Path("./test/"),
            output_file= Path("/output/birth-age.json") if execute_in_docker else Path("./output/birth-age.json")
        )
        
        # use GPU if available otherwise CPU
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print("===> Using ", self.device)

        #This path should lead to your model weights
        if execute_in_docker:
            self.path_model = "/opt/algorithm/checkpoints/ckpt.pth"
        else:
            self.path_model = "./weights/ckpt.pth"

        #Model hyperparameters
        self.dim = 192
        self.depth = 12
        self.heads = 3
        self.mlp_dim = 768 
        self.pool = 'cls'
        self.num_patches = 320
        self.num_classes = 1
        self.num_channels = 4
        self.num_vertices = 153
        self.dim_head = 64

        #You may adapt this to your model/algorithm here.
        self.model = SiT(dim=self.dim,
                        depth=self.depth,
                        heads=self.heads,
                        mlp_dim=self.mlp_dim,
                        pool=self.pool, 
                        num_patches=self.num_patches,
                        num_classes=self.num_classes,
                        num_channels=self.num_channels,
                        num_vertices=self.num_vertices,
                        dim_head=self.dim_head,)
        #loading model weights
        self.model.load_state_dict(torch.load(self.path_model,map_location=self.device),strict=False)
    
    def save(self):
        with open(str(self._output_file), "w") as f:
            json.dump(self._case_results[0], f)

    def process_case(self, *, idx, case):

        # Load and test the image for this case
        input_image, _ = self._load_input_image(case=case)
        # Detect and score candidates
        prediction = self.predict(input_image=input_image)
        # Return a float for prediction
        return float(prediction)

    def extract_sequence(self, image):

        if execute_in_docker:
            self.triangle_indices = pd.read_csv('/opt/algorithm/utils/triangle_indices_ico_6_sub_ico_2.csv')
        else:
            self.triangle_indices = pd.read_csv('./utils/triangle_indices_ico_6_sub_ico_2.csv')

        # patch the data
        sequence = np.zeros((self.num_channels, self.num_patches, self.num_vertices))
        for j in range(self.num_patches):
            indices_to_extract = self.triangle_indices[str(j)].to_numpy()
            sequence[:,j,:] = image[:,indices_to_extract]

        return torch.from_numpy(sequence).float()

    def predict(self, *, input_image: SimpleITK.Image) -> Dict:

        # Extract a numpy array with image data from the SimpleITK Image
        image_data = SimpleITK.GetArrayFromImage(input_image)

        ###  TODO: adapt this part for submission

        ## input image of shape (N vertices, C channels)
        if image_data.shape[0]==4:
            pass
        else:
            image_data = np.transpose(image_data, (1,0))
            
        # convert image into sequence of patches
        image_sequence = self.extract_sequence(image_data)
        image_sequence = image_sequence.unsqueeze(0)

        with torch.no_grad():

            prediction = self.model(image_sequence)
        
        return prediction.cpu().numpy()[0][0]

if __name__ == "__main__":

    Slcn_algorithm().process()

    
