from threading import Thread

counter = 0

def increment_counter_by(n):
    global counter
    for i in range(n):
        counter += 1


def main():
    t1 = Thread(target=increment_counter_by, args=(1000000, ))
    t2 = Thread(target=increment_counter_by, args=(1000000, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Counter: {counter}")


if __name__ == '__main__':
    main()