import java.util.Scanner;

//Find the hypotenuse 

public class Aula07_v2 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter side x: ");
        double x = scanner.nextDouble();

        System.out.println("Enter side y: ");
        double y = scanner.nextDouble();

        double a = ((x*x)+(y*y));
        double z = Math.sqrt(a);

        System.out.println("The hypotenuse is: "+z);
        
        scanner.close();
    }
}
