from threading import Thread
from math import ceil
from timeit import default_timer
from time import sleep

BUFFER_SIZE = 1 << 27
PARTITION_SIZE = 1 << 24

def sum_partition(buffer, low, high, results, current_partition):
    _sum = sum(buffer[low:high+1])
    results[current_partition] = _sum

def main():
    buffer = list(range(1, BUFFER_SIZE+1, 1))
    print("Allocated buffer")

    n_partitions = ceil(len(buffer) / PARTITION_SIZE)
    results = [0] * n_partitions
    threads = []
    current_partition = 0

    counter = 3
    while counter > 0:
        print(f"Starting threads in {counter}")
        sleep(1)
        counter -= 1

    print("Starting threads")
    start = default_timer()
    for i in range(0, len(buffer), PARTITION_SIZE):
        low = i
        high = min((i + PARTITION_SIZE), len(buffer)) - 1
        threads.append(Thread(target=sum_partition, args=(buffer, low, high, results, current_partition,)))
        current_partition += 1

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    res = sum(results)
    end = default_timer()
    print("Sum result: ", res)
    print("Time taken: ", (end - start) * 1000, "ms")
    

if __name__ == '__main__':
    main()

