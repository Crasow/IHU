using System;
using System.Text;

namespace OOP
{
    class Program
    {
        static int[] CreateVektor(int[,] arr, int len)
        {
            int[] vektor = new int[len];
            vektor[3] = 1;
            vektor[2] = 1;

            for (int i = 0; i <= arr.GetUpperBound(1); i++)
            {
                vektor[0] += arr[1, i];
            }
            for (int i = 0; i <= arr.GetUpperBound(1); i++)
            {
                vektor[1] -= arr[3, i];
            }
            for (int i = 0; i <= arr.GetUpperBound(0); i++)
            {
                vektor[2] *= arr[i, 5];
            }
            for (int i = 0; i <= arr.GetUpperBound(0); i++)
            {
                vektor[3] -= arr[i, 7];
            }


            return vektor;
        }
        static int[,] CreateArr(int rows, int cols, int from, int to)
        {
            int[,] arr = new int[rows, cols];
/*            Random rnd = new();
*/
            for (int i = 0; i <= arr.GetUpperBound(0); i++)
            {
                for (int j = 0; j <= arr.GetUpperBound(1); j++)
                {
/*                    arr[i, j] = rnd.Next(from, to + 1);
*/                }
            }
            return arr;
        }

        static void PrintVecrot(int[] arr)
        {
            Console.Write("\nВихiдний вектор: ");
            foreach (var item in arr)
            {
                Console.Write(item + " ");
            }
            Console.WriteLine();
        }
        static void PrintDoubleArr(int[,] arr)
        {
            for (int i = 0; i <= arr.GetUpperBound(0); i++)
            {
                for (int j = 0; j <= arr.GetUpperBound(1); j++)
                {
                    Console.Write("{0,5}", arr[i, j]);
                }
                Console.WriteLine();
            }

        }


        static void Main()
        {
            int[,] arr = CreateArr(10, 8, -16, 43);
            PrintDoubleArr(arr);
            int[] vektor = CreateVektor(arr, 4);
            PrintVecrot(vektor);
        }
    }
}