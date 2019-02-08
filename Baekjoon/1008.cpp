#include <iostream>

int main() {
    int a, b;        
    std::cin >> a >> b;

    std::cout.precision(15);
    std::cout << (long double)a / (long double)b;
    
}