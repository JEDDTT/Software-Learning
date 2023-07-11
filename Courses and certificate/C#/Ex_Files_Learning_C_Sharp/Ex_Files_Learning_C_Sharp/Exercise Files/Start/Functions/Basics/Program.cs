using System;

// Functions are used to group re-usable code together in a single
// unit that can be customized with parameters.
// TODO: Functions have a return type, name, and optional parameters
float MilesToKm(float miles)
{
    float result = miles * 1.6f;
    return result;
}
// TODO: A function with no return value has a 'void' type
void PrintWithPrefix(String thestr)
{
    Console.WriteLine($"::> {thestr}");
}
// TODO: Call first function
Console.WriteLine(MilesToKm(4f));
Console.WriteLine(MilesToKm(8f));
// TODO: Call second function
PrintWithPrefix("Emmanuel");
PrintWithPrefix("Ngongo");
