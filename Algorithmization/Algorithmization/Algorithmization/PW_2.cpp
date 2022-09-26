
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    double l, c, t;
    double u, k, y;

    std::cout << "Vvedit` c: ";
    std::cin >> c;
    std::cout << "Vvedit` t: ";
    std::cin >> t;
    l = pow(cos(c), 2) + (3 * pow(t, 2) + 4) / (sqrt(c + t));
    std::cout << "L = "<< l<<'\n';
    

    std::cout << "Vvedit` k: ";
    std::cin >> k;
    std::cout << "Vvedit` y: ";
    std::cin >> y;
    u = log(2*k+4.3)/pow(M_E, k+y)+sqrt(y);
    std::cout << "U = " << u << '\n';

    std::cout << "Konec \n";
    system("pause");
}