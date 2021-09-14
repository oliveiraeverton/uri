import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner input = new Scanner(System.in);
        int valor, a;
        valor = input.nextInt();
        for(int i = 0; i<valor; i++){
            a = input.nextInt();
            if(a==0){
                System.out.printf("NULL\n");
            }else{
                if(a%2==0){
                    System.out.printf("EVEN "); //positivo
                }else{
                    System.out.printf("ODD ");
                }
                if(a>0){
                    System.out.printf("POSITIVE\n");
                }else{
                    System.out.printf("NEGATIVE\n");
                }
            }
        }
 
    }
 
}
