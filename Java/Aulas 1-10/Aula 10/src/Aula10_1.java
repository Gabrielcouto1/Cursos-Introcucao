//switch statement

public class Aula10_1 {
    public static void main(String[] args) {
        
        String days = "pizza";

        switch(days){
            case "Sunday": System.out.println("It is sunday!");
            break;
            case "Monday": System.out.println("It is Monday!");
            break;
            case "Tuesday": System.out.println("It is Tuesday!");
            break;
            case "Wednesday": System.out.println("It is Wednesday!");
            break;
            case "Thursday": System.out.println("It is Thursday!");
            break;
            case "Friday": System.out.println("It is Friday!");
            break;
            case "Saturday": System.out.println("It is Saturday!");
            break;
            default: System.out.println(days+" is not a day.");
            break;
        }
    }
}
