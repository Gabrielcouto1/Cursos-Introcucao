//While loop

import java.util.Scanner;

public class Aula12_1 {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        String name = "";

        while(name.isBlank()){
            System.out.print("Enter your name: ");
            name = scanner.nextLine();           
        }
        
        System.out.println("Hello "+ name);

        scanner.close();
    }
}
