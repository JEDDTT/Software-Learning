using System;

// TODO: Functions can provide default values for their parameters
void PrintWithPrefix(string thestr, string prefix = "")
{
    Console.WriteLine($"{prefix} {thestr}");
}

// TODO: Test the default parameters
PrintWithPrefix("Emmanuel");
PrintWithPrefix("Emmanuel", "Mr. ");

// TODO: Call with named params
PrintWithPrefix(thestr: "Emmanuel", prefix: "BlackZ ");
