import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);//criando um obj do tipo input/scanner

        int[] vetor = new int[20];//criando um vetor
        
        // COLETANDO DO USUARIO OS 20 ELEMENTOS DO VETOR
        for(int i = 0; i < 20; i++){
            vetor[i] = input.nextInt();
        }
        int j = 20;
        //SUBSTITUINDO O PRIMEIRO ELEMENTOS COM O ÚLTIMO, ...,
        for(int i = 0; i < 10; i++){
            
            int elemento = vetor[j-1];
            vetor[j-1] = vetor[i];
            vetor[i] = elemento;
            j--;
        }

        //IMPRIMINDO OS 20 ELEMENTOS DO VETOR
        for(int i = 0; i < 20; i++){
            System.out.println("N["+i+"] = "+ vetor[i]);
        }
    }

}
