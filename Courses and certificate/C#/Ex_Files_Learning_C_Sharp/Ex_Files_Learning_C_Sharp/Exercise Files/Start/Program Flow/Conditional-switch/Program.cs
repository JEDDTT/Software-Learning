using System;

namespace ConditionalOps
{
    class Program
    {
        static void Main(string[] args)
        {
            int theVal = 50;

            // TODO: The switch statement
            switch (theVal)
            {
                case 50:
                    Console.WriteLine("The value is 50");
                    break;
                case 51:
                case 52:
                case 53:
                case 54:
                case 55:
                    Console.WriteLine("The value is between 51 and 55");
                    break;
                default:
                    Console.WriteLine("The value is something else");
                    break;
            }
        }
    }
}
