import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Pick a number between 1 to 10");
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();

        if (num >= 0 && num <= 5) {
            System.out.println("Enjoy the good luck of money and health coming to you");
        } else if (num >= 5 && num <= 10) {
            System.out.println("Enjoy the good luck of happiness and satisfaction coming to you");
        } else {
            System.out.println("Invalid Input, Choose a number between 1 and 10");
        }

    }
}