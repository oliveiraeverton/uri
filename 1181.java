import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
        float[][] matriz;
        
        matriz = new float[12][12];
        char operacao;
        int linha;
        Scanner input = new Scanner(System.in);
        linha = input.nextInt();
        operacao = input.next().charAt(0);;
        
        for(int i = 0; i < 12; i++){
            for(int j = 0; j < 12; j++){
                matriz[i][j] = input.nextFloat();
            }
        }
        float soma = 0;
        float media = 0;
        for(int j = 0; j < 12; j++){
            soma += matriz[linha][j];
        }
        media = soma/12;
        
        if(operacao == 'S'){
            System.out.printf("%.1f\n", soma);
        }else{
            System.out.printf("%.1f\n", media);
        }
    }
 
}
