SHELL := /bin/bash

default: build

build:
	@mkdir -p build 
	@g++ cpp/sum_partitions.cpp -pthread -o sum_partitions
	@g++ cpp/sum_traditional.cpp  -o sum_traditional
	@mv sum_partitions sum_traditional build
.PHONY: build

cpp_parallel: build
	./build/sum_partitions
.PHONY: cpp

cpp_single_thread: build
	./build/sum_traditional
.PHONY: cpp

python:
	python python/sum_partitions.py
.PHONY: python

clean:
	@rm -rf build
.PHONY: clean
