using System;

namespace ForLoops
{
    class Program
    {
        static void Main(string[] args)
        {
            int myVal = 15;
            int[] nums = new int[] { 3, 14, 15, 92, 6 };
            string str = "The quick brown fox jumps over the lazy dog";

            // TODO: the basic for loop
            Console.WriteLine("The basic for loop:");
            for (int i = 0; i < myVal; i++)
            {
                Console.WriteLine("The value of i is {0} ", i);
            }


            // TODO: the foreach-in loop can be used to iterate over sequences
            // Console.WriteLine("The foreach loop:");
            Console.WriteLine("-----------For each loop-----------------");
            foreach (int i in nums)
            {
                Console.WriteLine("The value of i is {0} ", i);
            }

            // TODO: count the number of o's in the string
            Console.WriteLine("--------------Counting o's in the string-----------");
            int count = 0;
            foreach (char c in str)
            {
                if (c == 'o')
                {
                    count++;
                }
            }
            Console.WriteLine("The number of o's in the string is {0}", count);

        }
    }
}
