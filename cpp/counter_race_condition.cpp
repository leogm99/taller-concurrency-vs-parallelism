#include <thread>
#include <iostream>

// en que segmento de memoria está esta variable?
// los threads posix comparten este segmento de memoria?
int counter = 0;


void increment_counter_by(int n) {
    for (int i = 0; i < n; ++i) {
        counter++;
    }
}

int main() {
    // spawn threads
    std::thread t1(increment_counter_by, 1000000);
    std::thread t2(increment_counter_by, 1000000);
    // join threads
    t1.join();
    t2.join();

    std::cout << "Counter: " << counter << std::endl;
    return 0;
}