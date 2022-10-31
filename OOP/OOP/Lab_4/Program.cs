using System;
using System.Text;

namespace OOP
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] mas1 = new int[5];
            int[] mas2 = new int[5];
            // Створення екземпляру генератора випадкових чисел
            Random rnd = new Random();
            // В циклі за допомогою метода Next генератора випадкових чисел
            // заповнюєто масив цілими числами в межах від 4 до 36 включно
            for (int i = 0; i < mas1.Length; i++)
            {
                mas1[i] = rnd.Next(-4, 18);
                mas2[i] = rnd.Next(-4, 18);

            }
            // Виводимо в консоль вихідний масив
            Console.Write("Вихідний масив1: ");
            foreach (var item in mas1)
            {
                Console.Write(item + " ");
            }
            Console.WriteLine();

            Console.Write("Вихідний масив2: ");
            foreach (var item in mas2)
            {
                Console.Write(item + " ");
            }
            Console.WriteLine();

            mas2[3] = mas1[3];

            for (int i = mas2.Length - 1; i != 3; i--)
            {
                mas1[i - 1] = mas1[i];
                mas1[i] = 0;
            }

            int[] new_mas1 = new int[4];

            for (int i = 0; i < new_mas1.Length; i++)
            {
                new_mas1[i] = mas1[i];
            }


            int prod = 1;

            foreach (var el in new_mas1)
            {
                prod *= el;
            }


            Console.Write("Вихідний масив1: ");
            foreach (var item in new_mas1)
            {
                Console.Write(item + " ");
            }
            Console.WriteLine();

            Console.Write("Вихідний масив2: ");
            foreach (var item in mas2)
            {
                Console.Write(item + " ");
            }
            Console.WriteLine();

            Console.WriteLine("prod of mas1 nums = " + prod);

            Console.Read();
        }
    }
}