/*using System;

namespace Lab_1
{
    internal class Lab_3
    {
        static void Main(string[] args)
        {
            double x, y, n;

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
                Console.WriteLine("Стала непередбачув" +
                    "ана помилка. Програма буде закрита.");
                Console.ReadLine();
                return;
            }

            if (x > 0 && y > 0)
            {
                n = 4;
            }
            else if (x < 0 && y < 0)
            {
                n = 2;
            }
            else if (Math.Abs(x) > Math.Abs(y))
            {
                n = 3;
            }
            else
            {
                n = 1;
            }
            Console.WriteLine($"Your dot is in {n} part");
            Console.ReadKey();
        }
    }
}
*/