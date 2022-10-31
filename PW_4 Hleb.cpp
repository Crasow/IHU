#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
using namespace std;


int main()
{
    int Ax, Ay, Bx, By, Alen, Blen;
    printf("Vvdeite Ax: ");
    cin >> Ax;
    printf("Vvdeite Ay: ");
    cin >> Ay;
    printf("Vvdeite Bx: ");
    cin >> Bx;
    printf("Vvdeite By: ");
    cin >> By;

    Alen = sqrt(pow(Ax, 2) + pow(Ay, 2));
    Blen = sqrt(pow(Bx, 2) + pow(By, 2));

    if (Alen > Blen) {
        printf("A is farer than B\n");

    }
    else {
        printf("B is farer than A\n");
    }

    system("pause");
    return 0;

}
