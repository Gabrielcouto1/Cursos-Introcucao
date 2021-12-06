//2D ArrayList  

import java.util.*;

public class Aula20 {
    public static void main(String[] args) {

        ArrayList<String> bakeryList = new ArrayList<String>();
        bakeryList.add("Pasta");
        bakeryList.add("Garlic bread");
        bakeryList.add("Donuts");

        ArrayList<String> produceList = new ArrayList<String>();
        produceList.add("Tomatoes");
        produceList.add("Zucchini");
        produceList.add("Peppers");

        ArrayList<String> DrinksList = new ArrayList<String>();
        DrinksList.add("Coffee");
        DrinksList.add("Soda");

        ArrayList<ArrayList<String>> groceryList = new ArrayList<ArrayList<String>>();

        groceryList.add(bakeryList);
        groceryList.add(produceList);
        groceryList.add(DrinksList);

        for(int i=0;i<groceryList.size();i++){
            System.out.println();
            for(int j=0;j<groceryList.get(i).size();j++){
                System.out.print(groceryList.get(i).get(j)+" ");
            }
        }
    }
}
