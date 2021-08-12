import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner input = new Scanner(System.in);
        int numero1, numero2;
        
        numero1 = input.nextInt();
        numero2 = input.nextInt();
        
        System.out.printf("PROD = %d%n", numero1*numero2);
 
    }
 
}
