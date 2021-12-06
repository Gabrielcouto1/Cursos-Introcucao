// overloaded methods = methods that share the same name but have different parameters
//						method name + parameters = method signature
public class Aula23 {
    public static void main(String[] args) {
        int x = add(3,4,5,6);
        System.out.println(x);
    } 

    static int add(int a,int b){
        return a+b;
    }
    static int add(int a,int b,int c){
        return a+b+c;
    }
    static int add(int a,int b,int c,int d){
        return a+b+c+d;
    }

}
