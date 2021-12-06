// method = a block of code that is executed whenever it is called upon

public class Aula22_1 {
    public static void main(String[] args) {
        String name = "Gabriel";
        int age = 19;

        hello(name,age);
    }

    static void hello(String name, int age){
        System.out.println("Hello "+name+"!!");
        System.out.println("You are "+age+" years old.");
    }
}
