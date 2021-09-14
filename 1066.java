import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner input = new Scanner(System.in);
        int par=0, impar=0, positivo=0, negativo=0, entrada;
        for(int i = 0; i<5; i++){
            entrada = input.nextInt();
            if (entrada >0){positivo++;}
            if (entrada < 0){negativo++;}
            if (entrada % 2 ==0){par++;}else{impar++;}
            
        }
        System.out.printf("%d valor(es) par(es)\n", par);
        System.out.printf("%d valor(es) impar(es)\n", impar);
        System.out.printf("%d valor(es) positivo(s)\n", positivo);
        System.out.printf("%d valor(es) negativo(s)\n",negativo);
 
    }
 
}
