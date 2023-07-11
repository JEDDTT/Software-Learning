using System;

namespace ProgChallengeStart
{
    class Program
    {
        static void Main(string[] args)
        {
            // Choose a random number between 0 and 20
            int theNumber = new Random().Next(20);

            // Print the game greeting and instructions
            Console.WriteLine("Let's Play 'Guess the Number'!");
            Console.WriteLine("I'm thinking of a number between 0 and 20.");
            Console.WriteLine("Enter your guess, or -1 to stop the game.");

            // Keep track of the number of guesses and the current user guess
            int guessCount = 0;
            int currentGuess = 0;

            // Start the game and run until user quits or guesses correctly
            // HINT: You'll need a way to convert the user's input to an integer
            //While loop is not appropriate 
            //      USING DO LOOP 
            do
            {
                Console.WriteLine("What is your guess");
                String input = Console.ReadLine();
                // Converting the input using try parse
                bool succeeded = false;
                succeeded = Int32.TryParse(input, out currentGuess);
                //if the input conversion is successful we compare it with the the random number
                if (succeeded)
                {
                    guessCount++;
                    if (currentGuess == theNumber)
                    {
                        Console.WriteLine($"You got it in {guessCount} guesses");
                    }
                    else if (currentGuess >= 0 && currentGuess < theNumber)
                    {
                        Console.WriteLine($"Nope, Higher than that");
                    }
                    else if (currentGuess > theNumber)
                    {
                        Console.WriteLine($"Nope, lower than that");
                    }
                }
                else
                {
                    Console.WriteLine("Hum, that doesn't look like a number, try again");
                }
            } while (currentGuess != -1);
        }
    }
}
