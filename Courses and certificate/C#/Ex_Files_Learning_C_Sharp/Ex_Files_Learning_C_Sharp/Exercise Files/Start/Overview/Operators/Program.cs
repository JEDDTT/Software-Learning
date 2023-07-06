using System;

namespace Operators
{
    class Program
    {
        static void Main(string[] args)
        {
            // Declare some variables to excercise the operators
            int x = 10, y = 5;
            string a = "abcd", b = "efgh";

            // TODO: Basic math operators are +, -, /, *
            Console.WriteLine("----- Basic Math -----");
            int add = x + y;
            Console.WriteLine(add);
            int substr = x - y;
            Console.WriteLine(substr);
            int div = x / y;
            Console.WriteLine(div);
            int mul = x * y;
            Console.WriteLine(mul);



            // TODO: Increment / decrement operators
            Console.WriteLine("----- Shorthand -----");
            x++;
            Console.WriteLine(x);
            y--;
            Console.WriteLine(y);

            // TODO: Operators can be shorthand: a = a + b
            Console.WriteLine(a += b); //short hand for a = a + b

            // TODO: Logical operators &&, ||
            Console.WriteLine("----- Logic Operators -----");
            Console.WriteLine(x > y && y >= 5); // It is false because of the y-- decrementation up there!!
            Console.WriteLine(x > y || y >= 5);



            // null-coalescing operators
            string str = null;
            // TODO: the ?? operator uses left operand if not null, or right one if it is
            Console.WriteLine(str ?? "Not null String");

            // TODO: the ??= operator assigns the right operand if the left one is null
            // it replaces the code:
            // if (variable is null) {
            //    variable = somevalue;
            // }
            str ??= "New String";
            Console.WriteLine(str);
        }
    }
}
