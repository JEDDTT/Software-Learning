namespace ProgChallenge;
using System;
using System.Text;
class Program
{
    // IsPalindrome returns a tuple of two values
        (bool, int) isPalindrome(string thestr) {
            string teststr;
            // Convert the string to upper-case
            teststr = thestr.ToUpper();

            //Use a stringBuilder to take out all the punctuation
            var sb = new StringBuilder();
            foreach (char c in teststr)
            {
                // Add characters to the builder if not punctuation or white space
                if (!char.IsPunctuation(c) && !char.IsWhiteSpace(c)) 
                {
                    sb.Append(c);
                }
            }
            // Convert the builder to the finished string
            teststr = sb.ToString();
            //Compare characters starting at the beginning and end of string
            int i=0, j=teststr.Length-1 //minus one because the index starts with zero
            //if the indexes cross each other, then we are done
            while (i <= j)
            {
                //If the character at each index doesn't match, it's not a palindrome
                if (teststr[i] != teststr[j])
                {
                    return(false, 0);
                }
                // Update the counters and try again
                i++;
                j--;
            }
            // if we reach this point, we must have a palindrome
            return(true, thestr.Length);
        }
        String inputstr = "";
        (bool b, int l) result:
        Console.WriteLine("Let's begin:");
        while (inputstr != "exit") 
        {
            inputstr = Console.ReadLine();
            if (inputstr != "exit") {
                result = isPalindrome(inputstr);
                Console.WriteLine($"Palindrome: {result.b}, Length: {result.l}");
            }
        }
}
