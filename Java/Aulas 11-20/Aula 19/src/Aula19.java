// ArrayList = 	a resizable array. 
//				Elements can be added and removed after compilation phase
//				store reference data types

import java.util.ArrayList;

public class Aula19 {
    public static void main(String[] args) {
        ArrayList<String> food = new ArrayList<String>();

        food.add("pizza");
        food.add("hamburger");
        food.add("hotdog");

        food.set(0,"sushi");    //.set(index,"value");
        food.remove(2);         //.remove(index)
        food.clear();           //clears ArrayList
        
        for(int i=0;i<food.size();i++){
            System.out.println(food.get(i));
        }
    }
}
