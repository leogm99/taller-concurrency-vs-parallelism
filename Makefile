SHELL := /bin/bash

default: build

build:
	@mkdir -p build 
	@g++ cpp/sum_partitions.cpp -pthread -o sum_partitions
	@g++ cpp/sum_traditional.cpp -o sum_traditional
	@g++ cpp/counter_race_condition.cpp -pthread -o counter_race_condition
	@mv sum_partitions sum_traditional counter_race_condition build
.PHONY: build

cpp_parallel: build
	./build/sum_partitions
.PHONY: cpp_parallel

cpp_single_thread: build
	./build/sum_traditional
.PHONY: cpp_single_thread

cpp_counter_race_condition: build
	./build/counter_race_condition
.PHONY: counter_race_condition

python_parallel:
	python3 python/sum_partitions.py
.PHONY: python_parallel

python_single_thread:
	python3 python/sum_traditional.py
.PHONY: python_single_thread

python_counter_race_condition: build
	python3 python/counter_race_condition.py
.PHONY: counter_race_condition

clean:
	@rm -rf build
.PHONY: clean
