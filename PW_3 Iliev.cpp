#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
using namespace std;


int main()
{
    double y, x;



    cout << "Vvedit` x: ";
    cin >> x;
    y = (2 * x + sin(x)) / (pow(cos(x), 2) + pow(x, 2)) + pow(0.5, x) / sqrt(x);
    cout << "y = " << y << '\n';


    std::cout << "Konec \n";
    system("pause");
    return 0;
}
