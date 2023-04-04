from timeit import default_timer

BUFFER_SIZE = 1 << 27

def main():
    buffer = list(range(1, BUFFER_SIZE+1, 1))
    start = default_timer()
    res = sum(buffer)
    end = default_timer()
    print("Result: ", res)
    print("Time taken:", (end - start)*1000, "ms")

if __name__ == '__main__':
    main()