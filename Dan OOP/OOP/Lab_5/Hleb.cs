/*namespace Lab_5
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

        static int[] NewArrWithOnes(int[] arr, int from, int ones_qty)
        {
            int[] newArr = new int[arr.Length + ones_qty];

            int cnt = 0;
            for (int i = 0; i < newArr.Length; i++)
            {
                if (i >= from && i <= (from + ones_qty - 1))
                {
                    newArr[i] = 1;

                }
                else
                {
                    newArr[i] = arr[cnt];
                    cnt++;
                }
            }

            return newArr;
        }

        static int ArrMin(int[] arr)
        {
            int min = arr[0];
            foreach (var item in arr)
            {
                if (item < min)
                {
                    min = item;
                }
            }
            return min;
        }


        static void Main()
        {
            int[] arr = ArrayCreate(10, 0, 40);
            ArrayPrint(arr);
            int[] new_arr = NewArrWithOnes(arr, 5, 3);
            ArrayPrint(new_arr);
            int new_arr_min = ArrMin(new_arr);
            Console.WriteLine(new_arr_min);
        }
    }
}
*/