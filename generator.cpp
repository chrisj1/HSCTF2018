// generator.cpp
#include <iostream>
#include <random>
using namespace std;
int main() {
    random_device seed_gen;
    mt19937 mt(seed_gen());
    for (int i = 0; i < 1000; ++i) {
        cout << mt() << endl;
    }
    return 0;
}
