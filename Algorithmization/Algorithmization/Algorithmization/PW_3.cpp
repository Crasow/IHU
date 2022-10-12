#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
using namespace std;


int main()
{
    double y, x;



    cout << "Vvedit` x: ";
    cin >> x;
    y = (3 * pow(x, 2) + 2 * x) / (sin(x) + pow(x, 2)) - (2 * x) / ((1 - pow(x, 2)) * (1 + 2 * x));
    cout << "y = " << y << '\n';


    std::cout << "Konec \n";
    system("pause");
    return 0;
}
