#include <vector>
#include <utility>
#include <iostream>
#include <thread>
#include <numeric>
#include <algorithm>


const std::size_t BUFFER_SIZE = 1ULL << 28; // 2**28 (256Mb)
const std::size_t PARTITION_SIZE = 1ULL << 25; // n_threads = ceil(BUFFER_SIZE / PARTITION_SIZE)

void sum_partition(const std::vector<uint64_t>& buffer, std::size_t low, std::size_t high, std::vector<uint64_t>& results, std::size_t partition) {
  uint64_t sum = 0;
  for (auto i = low; i <= high; ++i) {
    // forces this thread to yield execution
    std::this_thread::yield();
    sum += buffer[i];
  }
  results[partition] = sum;
}

int main() {
  std::vector<uint64_t> buffer(BUFFER_SIZE);
  std::iota(buffer.begin(), buffer.end(), 1);

  std::size_t n_partitions = buffer.size() / PARTITION_SIZE + ((buffer.size() % PARTITION_SIZE) == 0 ? 0 : 1);

  std::vector<uint64_t> results;
  results.resize(n_partitions, 0);

  std::vector<std::thread> threads;
  threads.reserve(n_partitions);

  auto current_partition = 0;
  for (std::size_t i = 0; i < buffer.size(); i+=PARTITION_SIZE) {
    auto low = i;
    auto high = std::min((i+PARTITION_SIZE), buffer.size()) - 1;
    threads.emplace_back(sum_partition, std::ref(buffer), low, high, std::ref(results), current_partition++);
  }

  for (auto& t : threads) {
    t.join();
  }
  uint64_t res =  std::accumulate(results.begin(), results.end(), 0ULL);
  std::cout << res << std::endl;
  return 0;
}
