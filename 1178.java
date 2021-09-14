import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);//criando um obj do tipo input/scanner

        double[] vetor = new double[100];//criando um vetor
        double valorEntrada;
        valorEntrada = input.nextDouble();
        vetor[0] = valorEntrada;
        int j = 1;
    
        for(int i = 0; i < 100; i++){
            System.out.printf("N[%d] = %.4f\n", i, vetor[i]);
           // System.out.println("N["+i+"] = "+ vetor[i]);
            if(j<100){vetor[j] = vetor[i] / 2.0f;}
            j++;
        }
    }
}
