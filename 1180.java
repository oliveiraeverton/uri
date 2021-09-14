import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner input = new Scanner(System.in);
        long[] vetor;
        int quantidadeElementos; 
        quantidadeElementos = input.nextInt();
        vetor = new long[quantidadeElementos];
        
        for(int i = 0; i < quantidadeElementos; i++){
            vetor[i] = input.nextLong();
        }
        long posicao, menorValor;
        menorValor = vetor[0];
        posicao = 0;
        for(int i = 1; i < quantidadeElementos; i++){
            if(menorValor > vetor[i]){
                menorValor = vetor[i];
                posicao = i;
            }
        }
        System.out.println("Menor valor: "+ menorValor+"\nPosicao: "+posicao);
    }
 
}
