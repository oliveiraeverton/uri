import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);//criando um obj do tipo input/scanner

        float[] vetor = new float[100];//criando um vetor
        
        
        for(int i = 0; i < 100; i++){
            vetor[i] = input.nextFloat();

            if (vetor[i]<=10){
                System.out.println("A["+i+"] = "+ vetor[i]);
            }
        }
    }
}
