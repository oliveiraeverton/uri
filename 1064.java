import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        float valor, soma=0, positivo=0, media=0;
        Scanner input = new Scanner(System.in);

        for(int i = 0; i<6; i++){

            valor = input.nextFloat();
            if(valor>= 0){
                positivo++;
                soma = soma + valor;
                
            }
            media = soma/positivo;
        }
        System.out.printf("%.0f valores positivos\n", positivo);
        System.out.printf("%.1f\n", media);
 
    }
 
}
