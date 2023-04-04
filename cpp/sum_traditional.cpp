#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <chrono>

const std::size_t BUFFER_SIZE = 1ULL << 27;	// 2**27

int main() {
    std::cout << "Allocating buffer of " << BUFFER_SIZE << " elements (" << sizeof(uint64_t) * ((float) BUFFER_SIZE / (float)(1ULL << 30)) << " GiB)\n";
	std::vector<uint64_t> buffer(BUFFER_SIZE);
	std::cout << "Allocated\n";
	std::iota(buffer.begin(), buffer.end(), 1);

    auto start = std::chrono::high_resolution_clock::now();
    uint64_t res = std::accumulate(buffer.begin(), buffer.end(), 0ULL);
    auto end = std::chrono::high_resolution_clock::now();

    std::cout << "Result: " << res << std::endl;
	std::cout << "Time taken: " << std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count() << "ms";
    return 0;
}
