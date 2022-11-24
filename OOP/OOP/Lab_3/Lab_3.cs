/*using System;
using System.Text;

namespace OOP
{
    class Program
    {
        static void Main(string[] args)
        {
            double dblY;

            for (double a = 0.5; a <= 2; a += 0.5)
            {
                // Вивід значення a
                Console.WriteLine("\nЗначення параметра а = {0}", a);
                Console.WriteLine("--------------------------------------------------");

                for (double x = -2; x <= 2; x += 0.05)
                {
                    dblY = Math.Pow(a, 3) / (Math.Pow(a, 2) + Math.Pow(x, 2));

                    Console.WriteLine("Аргумент х = {0, 3:f2}; Значення функції у = {1, 3:f3}", x, dblY);

                }
            }



            Console.WriteLine("Введіть аргумент х: ");
            double dblX = double.Parse(Console.ReadLine());
            double dblLast;
            const double TOCHNOST = 1e-6;
            double dblS = dblX;
            double dbln = 1;
            double dblF = 1;

            do
            {

                for (double FCnt = 1; FCnt <= dbln * 2; FCnt++)
                {
                    dblF *= FCnt;
                }

                dblLast = Math.Pow(-1, dbln) * Math.Pow(2, 2 * dbln) * Math.Pow(dblX, 2 * dbln + 1) / dblF;
                dblS += dblLast;
                dblF = 1;
                dbln++;
            } while (Math.Abs(dblLast) > TOCHNOST);

            Console.WriteLine("Результат розрахунку ряду S = {0:n3}", dblS);

            dblY = dblX * Math.Cos(2 * dblX);
            Console.WriteLine("Результат контрольного розрахунку у = {0:n3}", dblY);
            Console.Read();

        }
    }
}*/