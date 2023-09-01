#include <iostream>

int main( void )
{
    int a;
    std::cout << "Podaj a: ";
    std::cin >> a;
   
    int b;
    std::cout << "Podaj b: ";
    std::cin >> b;
   
    std::cout << "a % b = " << a % b << std::endl;
    return 0;
}