// printf() = 	an optional method to control, format, and display text to the console window
//				two arguments = format string + (object/variable/value)
//				% [flags] [precision] [width] [conversion-character]

public class Aula24 {
    public static void main(String[] args) {
        
        boolean myBoolean = true;
        char myChar = '@';
        String myString = "Gabriel";
        int myInt = 50;
        double myDouble = 1000;

        System.out.printf("%b\n",myBoolean);
        System.out.printf("%c\n",myChar);
        System.out.printf("%s\n",myString);
        System.out.printf("%d\n",myInt);
        System.out.printf("%.2f\n",myDouble);
        
        //[width]
		// minimum number of characters to be written as output
		System.out.printf("Hello %10s\n",myString);

        //[precision]
		// sets number of digits of precision when outputting floating-point values
		System.out.printf("You have this much money: %.2f\n",myDouble);

        // [flags]
		// adds an effect to output based on the flag added to format specifier
		// - : left-justify
		// + : output a plus ( + ) or minus ( - ) sign for a numeric value
		// 0 : numeric values are zero-padded
		// , : comma grouping separator if numbers > 1000

        System.out.printf("You have this much money: %,f\n",myDouble);
    }
}
