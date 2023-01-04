/*using System;


namespace Lab_1
{
    internal class Lab_2
    {
        static void Main(string[] args)
        {
            double x = 0, y = 0;
            int intN = 0;
            try
            {
                // Заповнення даних введених з клавіатури
                Console.WriteLine("Enter х");
                x = double.Parse(Console.ReadLine());
                Console.WriteLine("Enter y");
                y = double.Parse(Console.ReadLine());
            }
            // Блок catch для обробки виключення типу FormatException
            catch (FormatException)
            {
                Console.WriteLine("Дані введені невірно. Запустіть програму ще раз.");
                Console.ReadLine();
                return;
            }
            // Блок catch для обробки будь-якого типу виключень
            catch (Exception)
            {
                Console.WriteLine("Стала непередбачувана помилка. Програма буде закрита.");
                Console.ReadLine();
                return;
            }




            if (Math.Sqrt(x * x + y * y) < 12)
            {

                if (y >= x * x + 1)
                {
                    intN = 2;
                }
                else if (y > 0 & x < 0 & y <= x * x)
                {
                    intN = 1;
                }
                else
                {
                    intN = 3;
                }
            }
            else
            {
                intN = 4;
            }

            Console.WriteLine($"Your dot is in {intN} part");


            Console.ReadKey();


        }
    }
}
*/