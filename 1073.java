import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner input = new Scanner(System.in);
        int valor;
        valor = input.nextInt();
        
        for(int i = 2; i <= valor; i=i+2){
            System.out.printf("%d^2 = %d\n",i, i*i);
        }
    }
}
