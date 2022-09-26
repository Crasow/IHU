using System;


namespace Lab_1
{
    internal class Lab_2
    {
        static void Main(string[] args)
        {
            m1:
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


            if (x < 0 && y > 0)
            {
                intN = 3;
            }
            else if (x > 0 && y < 0)
            {
                intN = 4;
            }
            else if (x > 0 && y > 0)
            {
                if (y >= Math.Pow(x, 3))
                {
                    intN = 1;
                }

                else { intN = 4; }
            }
            else if (x < 0 && y < 0)
            {
                if (y <= Math.Pow(x, 3))
                {
                    intN = 2;
                }
                else { intN = 3; }
            }

            Console.WriteLine($"Your dot is in {intN} part");

            Console.Write("Do you want to continiue Y/N: ");
            string s = Console.ReadLine();
            if (s == "Y" || s == "y") goto m1;

            Console.ReadKey();


        }
    }
}
