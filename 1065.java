import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        int inteiro;
        int par = 0;
        Scanner input = new Scanner(System.in);
        
        for(int i = 0; i < 5; i++){
            inteiro = input.nextInt();
            if(inteiro%2==0){
                par++;
            }
        }
        System.out.println(par+" valores pares");
 
    }
 
}
