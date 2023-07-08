using System;

namespace Operations
{
    class Program
    {
        static void Main(string[] args)
        {
            // Declare some strings for the exercises
            string outstr = "C.";
            string str1 = "The quick brown fox jumps over the lazy dog.";
            string str2 = "This is a string";
            string str3 = "THIS is a STRING";
            string[] strs = { "one", "two", "three", "four" };

            // TODO: Length of a string 
            Console.WriteLine(str1.Length);

            // TODO: Access individual characters
            Console.WriteLine(str1[14]);

            // TODO: iterate over a string like any other sequence of values
            foreach (char c in str1)
            {
                Console.WriteLine(c);
                if (c == 'j')
                {
                    break;
                }

            }

            // TODO: String Concatenation         
            outstr = String.Concat(str1);
            //str2 = String.Concat(str1);
            // Concat method replace the first string with the second string.
            Console.WriteLine(outstr);
            // Console.WriteLine(str2);


            // TODO: Joining strings together with Join
            outstr = String.Join(":", strs);
            Console.WriteLine(outstr);
            outstr = String.Join("-", strs);
            Console.WriteLine(outstr);

            // TODO: String Comparison
            // Compare will perform an ordinal comparison and return:
            // < 0 : first string comes before second in sort order
            // 0 : first and second strings are same position in sort order
            // > 0 : first string comes after the second in sort order
            int result = String.Compare(str2, "This is a string");
            Console.WriteLine("{0}", result);

            // TODO: Equals just returns a regular Boolean
            bool isEqual = str2.Equals(str3);
            Console.WriteLine("{0}", isEqual);

            // TODO: String Searching
            Console.WriteLine("{0}", str1.IndexOf("h"));
            Console.WriteLine("{0}", str1.IndexOf("t"));

            Console.WriteLine("{0}", str1.LastIndexOf("e"));
            Console.WriteLine("{0}", str1.LastIndexOf("n"));

            outstr = str1.Replace("fox", "dog");
            Console.WriteLine("{0}", outstr);
        }
    }
}
