import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);//criando um obj do tipo input/scanner

        int[] vetor = new int[10];//criando um vetor
        int valorEntrada;
        valorEntrada = input.nextInt();
        vetor[0] = valorEntrada;
        for(int i = 1; i < 10; i++){
            vetor[i] = vetor[i-1] * 2;
            
        }
        for(int i = 0; i < 10; i++){
            System.out.println("N["+i+"] = "+ vetor[i]);
        }
    }


}
