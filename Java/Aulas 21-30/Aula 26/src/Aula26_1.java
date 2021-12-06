//  OOP1

public class Aula26_1 {
    public static void main(String[] args) {

        Car myCar = new Car();

        System.out.println(myCar.model);
        myCar.drive();

        myCar.color = "Red";

        System.out.println(myCar.color);
    }
}