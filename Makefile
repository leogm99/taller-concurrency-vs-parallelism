SHELL := /bin/bash

default: build

build:
	@mkdir -p build 
	@g++ cpp/sum_partitions.cpp -pthread -o sum_partitions
	@mv sum_partitions build
.PHONY: build

cpp: build
	./build/sum_partitions
.PHONY: cpp

python:
	python python/sum_partitions.py
.PHONY: python

clean:
	@rm -rf build
.PHONY: clean