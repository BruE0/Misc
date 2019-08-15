/*
C++
forest_fire.cpp
2019.08
*/


#include <iostream>
#include <fstream>
#include <array>


const int TOTAL = 20000;


bool three_points_same_distance(std::array<int, TOTAL> nums, int X) {
    for (int x=X-1; x>=X/2; --x) {
        if ((2*nums[x] - nums[X]) == nums[2*x - X]) {
            return true;
        }
    }
    return false;
}


std::array<int, TOTAL> forest_fire() {
    std::array<int, TOTAL> nums = {1,1};
    int attempt;
    for (int X=2; X<TOTAL; ++X) {
        std::cout << X << "\n";
        attempt = 1;
        while(1) {
            nums[X] = attempt;
            if (three_points_same_distance(nums, X)) {
                attempt += 1;
            } else {
                break;
            }
        }
    }
    return nums;
}


int main() {
    std::array<int, TOTAL> nums;
    nums = forest_fire();

    std::cout << "Writing to file" << "\n";
    std::ofstream my_file;
    my_file.open("test.txt");
    my_file << "[";
    for (int i=0; i<TOTAL-1; i++) {
        my_file << nums[i] << ", ";
    }
    my_file << nums[TOTAL-1] << "]" << "\n";
    my_file.close();
    return 0;
}
