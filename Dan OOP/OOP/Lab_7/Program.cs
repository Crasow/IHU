using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace Lab_7
{
    class Program
    {
        static void Main(string[] args)
        {
            // Встановлення значення назви фігури
            Console.Write("Введіть назву трикутника: ");
            string strName = Console.ReadLine();
            // Встановлення значення катета a
            Console.Write("Введіть довжину катета a: ");
            double dblLegA = double.Parse(Console.ReadLine());
            // Встановлення значення катета b
            Console.Write("Введіть довжину катета b: ");
            double dblLegB = double.Parse(Console.ReadLine());

            Console.WriteLine();
            // Створення нового екземпляра об'єкту за допомогою власного констуктора
            RightTriangle ABC = new RightTriangle(strName, dblLegA, dblLegB);
            // Далі йде вивід відомостей про об'єкт (фігуру)
            // шляхом безпосереднього доступу до властивостей та методів об'єкта
            Console.WriteLine("Назва фігури: " + ABC.Name);
            Console.WriteLine("Довжина катета a: {0,4:n2}", ABC.legA);
            Console.WriteLine("Довжина катета b: {0,4:n2}", ABC.legB);
            Console.WriteLine("Довжина сторони c: {0,4:n2}", ABC.legC());
            Console.WriteLine("Площа: {0,4:n2}", ABC.Area());
            Console.WriteLine("Периметр: {0,4:n2}", ABC.Perimeter());
            Console.WriteLine("Кут мiж сторонами b та с: {0,4:n2}", ABC.bcAngle());
            Console.WriteLine("Кут мiж сторонами a та с: {0,4:n2}", ABC.acAngle());
            // І нарешті автоматичний вивід відомостей про об'єкт (фігуру)
            // за допомогою спеціального метода об'єкта
            ABC.FigureInfo();
            Console.ReadLine();
        }
    }

    //Код класу RightTriangle
    class RightTriangle
    {
        public RightTriangle()
        {
        }
        public RightTriangle(string name, double a, double b)
        {
            Name = name;
            legA = a;
            legB = b;
        }
        // Використання автоматичної властивості
        public string Name { get; set; }
        // Внутрішня змінна, яка зберігає значення властивості Storona
        // Оголошення властивості Storona
        private double dblLegA;
        private double dblLegB;

        public double legA
        {
            get { return dblLegA; }
            set
            {
                // Здійснюється перевірка значення сторони квадрату
                if (value > 0)
                {
                    dblLegA = value;
                }
                else
                {
                    Console.WriteLine("Помилкове значення сторони!");
                }
            }
        }
        public double legB
        {
            get { return dblLegB; }
            set
            {
                if (value > 0)
                {
                    dblLegB = value;
                }
                else
                {
                    Console.WriteLine("Помилкове значення сторони!");
                }
            }
        }

        public double legC()
        {
            return Math.Sqrt(Math.Pow(dblLegA, 2) + Math.Pow(dblLegB, 2));
        }
        public double Perimeter()
        {
            return legB + legA + legC();
        }
        public double Area()
        {
            return (legA*legB)/2;
        }
        public double bcAngle()
        {
            return Math.Acos((legB * legB + legC() * legC() - legA * legA) / (2 * legB * legC())) * 180 / Math.PI;
        }

        public double acAngle()
        {
            return 180-90-bcAngle();
        }


        public void FigureInfo()
        {
            Console.WriteLine("Назва фігури: " + Name);
            Console.WriteLine("Довжина катета a: {0,4:n2}", legA);
            Console.WriteLine("Довжина катета b: {0,4:n2}", legB);
            Console.WriteLine("Довжина сторони c: {0,4:n2}", legC());
            Console.WriteLine("Площа: {0,4:n2}", Area());
            Console.WriteLine("Периметр: {0,4:n2}", Perimeter());
            Console.WriteLine("Кут мiж сторонами b та с: {0,4:n2}", bcAngle());
            Console.WriteLine("Кут мiж сторонами a та с: {0,4:n2}", acAngle());
        }
    }
}
