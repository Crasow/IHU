using System;


namespace Lab1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double x, y;
            int intN = 0;
            try
            {
                Console.WriteLine("Enter х");
                x = double.Parse(Console.ReadLine());
                Console.WriteLine("Enter y");
                y = double.Parse(Console.ReadLine());
            }
            catch (FormatException)
            {
                Console.WriteLine("Дані введені невірно. Запустіть програму ще раз.");
                Console.ReadLine();
                return;
            }
            catch (Exception)
            {
                Console.WriteLine("Стала непередбачувана помилка. Програма буде закрита.");
                Console.ReadLine();
                return;
            }

            if (x)







        }
    }
}