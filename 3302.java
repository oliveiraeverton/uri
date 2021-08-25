import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner input = new Scanner(System.in);
        
        int casoTeste, numero, i;
        i = 1;
        casoTeste = input.nextInt();
        while(casoTeste>0){
            casoTeste--;
            numero = input.nextInt();
            System.out.printf("resposta %d: %d\n",i ,numero);
            i++;
        }
 
    }
 
}
