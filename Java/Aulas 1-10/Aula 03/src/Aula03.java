// swap 2 variables

public class Aula03 {
    public static void main(String[] args) {
        
        String x = "Water";
        String y = "Kool-Aid";
        String temp = null;

        temp = x;
        x = y;
        y = temp;
        
        System.out.println("x: "+x);
        System.out.println("y: "+y);

    }
}