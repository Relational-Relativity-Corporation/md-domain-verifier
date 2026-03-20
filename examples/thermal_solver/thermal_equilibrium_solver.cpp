#include <iostream>
using namespace std;

int main() {
    double temperature = 100;
    double new_temp = temperature * 0.9; // diffusion

    double convection = new_temp * 0.1; // not declared

    cout << new_temp << endl;
    return 0;
}
