#include <random>
#include <iostream>
#include <vector>

int main() {
    std::mt19937 random;
    std::ios::sync_with_stdio(false);

    std::cout << "Welcome to the Yanny/Laurel simulator\n"
                 "In this game you will simulate what people hear\n"
                 "Do you have what it takes to identify the pattern?\n"
                 "Here, I'll give you some free responses (Y is Yanny, L is Laurel)" << std::endl;

    std::vector<uint32_t> nums; 
    for (int i = 0; i < 625; ++i) {
        bool printed = false;
        for (uint32_t j = 0, value = random(); j < 32; ++j, value >>= 1) {
            if(!printed) {
                nums.push_back(value);
                printed = true;
            }
            std::cout << (value & 1 ? "Y" : "L") << "\n";
        }
    }

    std::cout << "Okay, now predict some (again Y is Yanny and L is Laurel)" << std::endl;
    for (auto elem : nums) {
        std::cout << elem << std::endl;
    }
    for (uint32_t j = 0, value = random(); j < 32; ++j, value >>= 1) {
        std::cout << value << std::endl;
        std::string s;
        std::cin >> s;
        std::cout << (value & 1 ) << std::endl;
        std::cout << (s != "Y") << std::endl;
        std::cout << !(value & 1) << std::endl;
        std::cout << (s != "L") << std::endl;
        if (value & 1 && s != "Y" || !(value & 1) && s != "L") {
	    std::cout << "I'm sorry that is incorrect.\n"
                         "Goodbye!" << std::endl;
	    return 0;
        }
    }

    std::cout << "To get the flag, connect using netcat." << std::endl;

    return 0;
}