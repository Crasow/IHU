using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_5
{
	internal class Program
	{

		static int[] ArrayCreate(int qty, int min, int max)
		{
			int[] arr = new int[qty];
			Random rnd = new Random();
			for (int i = 0; i < arr.Length; i++)
			{
				arr[i] = rnd.Next(min, max);

			}
			return arr;

		}
		static void ArrayPrint(int[] arr)
		{
			Console.Write("Вихiдний масив: ");
			foreach (var item in arr)
			{
				Console.Write(item + " ");
			}
			Console.WriteLine();
		}

		static int[] ArrayToArray(int[] arr, int from, int to)
		{
			int[] new_arr = new int[to - from + 1];

			int cnt = 0;
			for (int i = from; i <= to; i++)
			{
				new_arr[cnt] = arr[i];
				cnt++;
			}

			return new_arr;
		}

		static int ArrSum(int[] arr)
		{
			int sum = 0;
			foreach (var item in arr)
			{
				sum += item;
			}
			return sum;
		}


		static void Main()
		{
			int[] arr = ArrayCreate(10, 4, 46);
			ArrayPrint(arr);
			int[] new_arr = ArrayToArray(arr, 4, 9);
			ArrayPrint(new_arr);
			int new_arr_sum = ArrSum(new_arr);
			Console.WriteLine(new_arr_sum);
			Console.Read();
		}
	}
}
