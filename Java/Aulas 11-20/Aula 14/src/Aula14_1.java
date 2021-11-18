//nested loops
import java.util.Scanner;

public class Aula14_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int rows;
        int columns;
        String symbol ="";

        System.out.println("Enter the number of rows: ");
        rows = scanner.nextInt();
        System.out.println("Enter the number of columns: ");
        columns = scanner.nextInt();
        System.out.println("Enter the symbol: ");
        symbol = scanner.next();

        for (int i=0;i<rows;i++){
            System.out.println();
            for(int j=0;j<columns;j++)
                System.out.print(symbol);
        }
        scanner.close();
    }  
}
