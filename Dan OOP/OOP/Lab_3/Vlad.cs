/*using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_3
{
    class Lab_3
    {
        static void Main(string[] args)
        {
            double dblY;

            for (double a = 0.5; a <= 1.25; a += 0.25)
            {
                // Вивід значення a
                Console.WriteLine("\nЗначення параметра а = {0}", a);
                Console.WriteLine("--------------------------------------------------");

                for (double x = 0; x <= 3; x += 0.1)
                {
                    dblY = Math.Atan(x / 2 * a) / Math.Pow(x, 2) + 2 * a;

                    Console.WriteLine("Аргумент х = {0, 3:f2}; Значення функції у = {1, 3:f3}", x, dblY);

                }
            }



            Console.WriteLine("Введіть аргумент х: ");
            double dblX = double.Parse(Console.ReadLine());
            double dblCyclePart;
            const double border = 1e-6;
            double dblResult = 1 + dblX * Math.Log(2);
            double Factor = 1;
            double Increment = 2;


            do
            {
                Factor *= Increment;
                dblCyclePart = Math.Pow(dblX, Increment) * Math.Pow(Math.Log(Increment), Increment) / Factor;
                dblResult += dblCyclePart;
                Increment++;

            } while (Math.Abs(dblCyclePart) > border);

            Console.WriteLine("Результат розрахунку ряду S = {0:n3}", dblResult);

            Console.Read();
        }
    }
}
*/