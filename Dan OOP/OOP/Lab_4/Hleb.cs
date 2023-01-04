/*namespace OOP
{
    class Program
    {
        static void Main(string[] args)
        {

            int[] mas1 = new int[6];
            int[] mas2 = new int[6];
            // Створення екземпляру генератора випадкових чисел
            Random rnd = new Random();
            // В циклі за допомогою метода Next генератора випадкових чисел
            // заповнюєто масив цілими числами в межах від 4 до 36 включно
            for (int i = 0; i < mas1.Length; i++)
            {
                mas1[i] = rnd.Next(1, 40);
                mas2[i] = rnd.Next(1, 40);

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


            int temp = mas2[1];

            for (int i = mas2.Length-1; i >2; i--)
            {
                mas2[i] = mas2[i - 1];
            }

            mas2[2] = mas1[2];

            

            Console.Write("Вихідний масив2: ");
            foreach (var item in mas2)
            {
                Console.Write(item + " ");
            }
            Console.WriteLine();


            int min = mas2[0];
            foreach (var item in mas2)
            {
                if (item < min)
                {
                    min = item;
                }
            }

            Console.WriteLine(min);
        }


    }

}*/