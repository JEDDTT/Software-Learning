using System;

namespace Exceptions
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 100;
            int y = 10;
            int result;

            // TODO: try-catch expressions make error checking easier
            try
            {
                if (x < 0 && x > 1000)
                {
                    throw new ArgumentOutOfRangeException("x", "x has be between 0 to 1000");
                }
                if (y < 0 && y > 1000)
                {
                    throw new ArgumentOutOfRangeException("y", "y has be between 0 to 1000");
                }
                result = x / y;
                Console.WriteLine("The result is: {0}", result);
            }
            catch (DivideByZeroException e)
            {
                Console.WriteLine("A zero division is not allowed");
                Console.WriteLine(e.Message);
            }
            catch (ArgumentOutOfRangeException e)
            {
                Console.WriteLine("Numbers should be between 0 to 1000");
                Console.WriteLine(e.Message);
            }
            finally
            {
                Console.WriteLine("this code always run ");
            }

        }
    }
}
