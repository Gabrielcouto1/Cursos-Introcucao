// String methods

public class Aula17 {
    public static void main(String[] args) {
        String name = "Gabriel";

        //boolean result = name.equals("gabriel");    //Returns true or false if equals
        //boolean result_1 = name.equalsIgnoreCase("gabriel");  // Ignores the lower and uppercase
        //int length = name.length();     //returns the length
        //char result = name.charAt(0);   //returns the char in the index of the string
        //int result = name.indexOf(a);     //Returns the position of the indicated char
        //boolean result = name.isEmpty();    //Returns true if the string is empty, false otherwise
        //String result = name.toUpperCase(); //returns to upper
        //String result = name.toLowerCase(); //returns to Lower
        //String result = name.trim();    //removes the useless empty spaces
        String result = name.replace('a','o');  //Replaces the first letter with the second letter

        System.out.println(result);
    }

}
