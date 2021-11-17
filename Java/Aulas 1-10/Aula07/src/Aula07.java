//Math class


public class Aula07 {
    public static void main(String[] args) {
        
        double x = 3.14;
        double y = -10;

        double y_1 = Math.abs(y);

        double z = Math.max(x, y);

        double w = Math.min(x, y);
        
        double sqrt = Math.sqrt(x);

        double piRound = Math.round(x); //Math.floor(x) rounds down and Math.ceil(x) rounds up

        System.out.println("The largest number is "+z);
        System.out.println("The smallest number is "+w);
        System.out.println("The absolute value of "+y+" is "+y_1);
        System.out.println("Squareroot: "+sqrt);
        System.out.println("Pi : "+piRound);
    }   
}
