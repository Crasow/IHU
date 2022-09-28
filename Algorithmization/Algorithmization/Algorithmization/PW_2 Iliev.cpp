
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    double V6, x, a;
    double u, k, y;

    std::cout << "Vvedit` k: ";
    std::cin >> k;
    std::cout << "Vvedit` y: ";
    std::cin >> y;    
    std::cout << "Vvedit` x: ";
    std::cin >> x;
    u = log(pow(x, 3) + y) - pow(y, 4) / pow(M_E, y) + 5.4 * pow(k, 3);
    std::cout << "U = " << u << '\n';

    std::cout << "Vvedit` x: ";
    std::cin >> x;
    std::cout << "Vvedit` a: ";
    std::cin >> a;
    V6 = pow(M_E, pow(log(pow(pow(x, 2) - 1.8, 3)), 3)) + pow(x, 4.5) / atan(pow(x, 2) + pow(a, 2))-sqrt(pow(x,3.2));
    std::cout << "V6 = " << V6 << '\n';




    std::cout << "Konec \n";
    system("pause");
}