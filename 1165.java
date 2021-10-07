import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner input = new Scanner(System.in);
        
        int casoTeste;
        
        casoTeste = input.nextInt();
        
        while(casoTeste>0){
            int primo;
            primo = input.nextInt();
            
            int divisores = 0;
            if(primo == 2){
                System.out.println("2 eh primo");
            }else if(primo == 1){
                System.out.println("1 nao eh primo");
            }else{
                for(int i = 2; i <= primo; i++){
                    if(primo%i==0){
                        divisores = divisores +1;
                    }
                }
                if(divisores == 1){
                    System.out.printf(primo+" eh primo\n");
                }else{
                    System.out.printf(primo+" nao eh primo\n");
                }
                
            }
            casoTeste--;
        }
 
    }
 
}
