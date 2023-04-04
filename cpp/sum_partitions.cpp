#include <vector>
#include <utility>
#include <iostream>
#include <thread>
#include <numeric>
#include <algorithm>
#include <chrono>
#include <utility>

const std::size_t BUFFER_SIZE = 1ULL << 27;	   // 2**27
const std::size_t PARTITION_SIZE = 1ULL << 24; // n_threads = ceil(BUFFER_SIZE / PARTITION_SIZE)

void sum_partition(const std::vector<uint64_t> &buffer, std::size_t low, std::size_t high, std::vector<uint64_t> &results, std::size_t partition){
	uint64_t sum = 0;
	for (auto i = low; i <= high; ++i){
		sum += buffer[i];
	}
	results[partition] = sum;
}

int main(){
	std::cout << "Allocating buffer of " << BUFFER_SIZE << " elements (" << sizeof(uint64_t) * ((float) BUFFER_SIZE / (float)(1ULL << 30)) << " GiB)\n";
	std::vector<uint64_t> buffer(BUFFER_SIZE);
	std::cout << "Allocated\n";
	std::iota(buffer.begin(), buffer.end(), 1);

	std::size_t n_partitions = buffer.size() / PARTITION_SIZE + ((buffer.size() % PARTITION_SIZE) == 0 ? 0 : 1);

	std::vector<uint64_t> results;
	results.resize(n_partitions, 0);

	std::vector<std::thread> threads;
	threads.reserve(n_partitions);

	int sec = 3;
	
	do {
		using namespace std::chrono_literals;
		std::cout << "Starting threads in " << sec << std::endl;
		std::this_thread::sleep_for(1000ms);
	} while(--sec > 0);

	std::cout << "Starting threads\n";
	auto start = std::chrono::high_resolution_clock::now();
	auto current_partition = 0;
	for (std::size_t i = 0; i < buffer.size(); i += PARTITION_SIZE){
		auto low = i;
		auto high = std::min((i + PARTITION_SIZE), buffer.size()) - 1;
		auto thread = std::thread(sum_partition, 
			std::ref(buffer),
			low,
			high,
			std::ref(results),
			current_partition++
		);
		threads.push_back(std::move(thread));
	}

	for (auto &t : threads){
		t.join();
	}

	uint64_t res = std::accumulate(results.begin(), results.end(), 0ULL);
	auto end = std::chrono::high_resolution_clock::now();
	std::cout << "Sum result: " << res << std::endl;
	std::cout << "Time taken: " << std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count() << "ms";
	return 0;
}
