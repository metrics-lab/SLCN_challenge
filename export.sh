#!/usr/bin/env bash

./build.sh

docker save slcn_algorithm | gzip -c > SLCN_algorithm.tar.gz
