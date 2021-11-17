//User inputs

import java.util.Scanner;

public class Aula04 {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);

        System.out.println("What is your name?");
        String name = scanner.nextLine();

        System.out.println("How old are you?");
        int age = scanner.nextInt();

        scanner.nextLine(); //you have to do this to scan the next input without any problems\
        //this is due to the nextLine scanning and the println

        System.out.println("What is your favorite food?");
        String food = scanner.nextLine();

        System.out.println("\nHello "+name);
        System.out.println("You are "+age+" years old.");
        System.out.println("\nyou like "+food);

        scanner.close();
    }
    
}
