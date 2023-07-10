using System;
using System.Text;

namespace Builder
{
    class Program
    {
        static void Main(string[] args)
        {
            int jumpCount = 10;
            string[] animals = { "dogs", "cats", "birds" };

            // TODO: create a StringBuilder
            StringBuilder sb = new StringBuilder("This is an initial string. ", 200);

            // TODO: print some basic stats about the StringBuilder
            Console.WriteLine($"The capacity is {sb.Capacity} and length is {sb.Length}");

            // TODO: Add some strings to the builder using Append
            sb.Append("Emmanuel means God amongst us.");
            sb.Append("I believe God is with me");

            // TODO: AppendLine can append a line ending
            //Console.WriteLine(sb);
            sb.AppendLine();

            // TODO: AppendFormat can be used to append formatted strings
            sb.AppendFormat($"I got to better myself everyday to be {jumpCount} times stronger ");
            sb.AppendFormat("I am {0} times better than the last year", jumpCount);
            sb.AppendLine();

            // TODO: AppendJoin can iterate over a set of values
            sb.Append("I love ");
            sb.AppendJoin(",", animals);

            // TODO: Modify the content using Replace
            sb.Replace(".", ":");

            // TODO: Insert content at any index
            sb.Insert(0, "------");
            Console.WriteLine($"The capacity is {sb.Capacity} and length is {sb.Length}");
            // TODO: Convert to a single string
            Console.WriteLine(sb.ToString());
        }
    }
}
