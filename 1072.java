import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
 
       Scanner input = new Scanner(System.in);
       int casoTeste=0, entrada=0, dentro=0, fora=0;
       
       casoTeste = input.nextInt();
       for(int i = 0; i<casoTeste; i++){
           
           entrada = input.nextInt();
           if(entrada>= 10 && entrada <=20)
           {
               dentro++;
           }
           else
           {
               fora++;
           }
       }
        System.out.printf("%d in\n",dentro);
        System.out.printf("%d out\n",fora);
    }
 
}
