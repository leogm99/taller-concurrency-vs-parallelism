from threading import Thread
from math import ceil

BUFFER_SIZE = 1 << 28
PARTITION_SIZE = 1 << 25

def sum_partition(buffer, low, high, results, current_partition):
    _sum = sum(buffer[low:high+1])
    results[current_partition] = _sum

def main():
    buffer = list(range(1, BUFFER_SIZE+1, 1))

    n_partitions = ceil(len(buffer) / PARTITION_SIZE)
    results = [0] * n_partitions
    threads = []
    current_partition = 0

    print("Starting threads")

    for i in range(0, len(buffer), PARTITION_SIZE):
        low = i
        high = min((i + PARTITION_SIZE), len(buffer)) - 1
        threads.append(Thread(target=sum_partition, args=(buffer, low, high, results, current_partition,)))
        current_partition += 1

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Result: ", sum(results))
    

if __name__ == '__main__':
    main()

