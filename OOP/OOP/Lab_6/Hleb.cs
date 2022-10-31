namespace OOP
{
    class Program
    {
        static int[,] CreateSmallMtrx(int[,] arr, int cols, int rows, int min, int max)
        {
            int[,] smallMtrx = new int[cols, rows];
            Random rnd = new();
            int upp_cnt = 0, bot_cnt = 0;

            for (int i = 0; i <= arr.GetUpperBound(0); i++)
            {
                for (int j = 0; j <= arr.GetUpperBound(1); j++)
                {
                    arr[i, j] = rnd.Next(min, max + 1);
                }
            }


            return smallMtrx;
        }
        static int[,] CreateMtrx(int rows, int cols, int min, int max)
        {
            int[,] arr = new int[rows, cols];
            Random rnd = new();

            for (int i = 0; i <= arr.GetUpperBound(0); i++)
            {
                for (int j = 0; j <= arr.GetUpperBound(1); j++)
                {
                    arr[i, j] = rnd.Next(min, max + 1);
                }
            }
            return arr;
        }


        static void PrintMtrx(int[,] arr)
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
            int min = -80, max = 80;
            int[,] mtrx = CreateMtrx(6, 8, min, max);
            PrintMtrx(mtrx);
            int[] smallMtrx = CreateSmallMtrx(mtrx, 4, 5, min, max);
        }
    }
}