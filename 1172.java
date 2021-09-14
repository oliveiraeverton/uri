import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);//criando um obj do tipo input/scanner

        int[] vetor = new int[10];//criando um vetor

        for(int i = 0; i < 10; i++){
            vetor[i] = input.nextInt();
            if (vetor[i] <= 0) {
                vetor[i] = 1;
            }
        }
        for(int i = 0; i < 10; i++){
            System.out.println("X["+i+"] = "+ vetor[i]);
        }
    }


}
