import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
        double[][] matriz;
        
        matriz = new double[12][12];
        char operacao;
        int linha;
        int coluna;
        
        Scanner input = new Scanner(System.in);
        
        operacao = input.next().charAt(0);;
        
        for(int i = 0; i < 12; i++){
            for(int j = 0; j < 12; j++){
                matriz[i][j] = input.nextDouble();
            }
        }
        
        
        double soma = 0;
        double media = 0;
        int elemento = 0;
        int retirar = 12;
        
        for(int i = 0; i < 12; i++){
            retirar--;
            for(int j = 0; j < retirar; j++){
                if(i<j){
                    soma += matriz[i][j];
                    elemento++;
                
                }
            }
        }
        media = soma/elemento;
        
        if(operacao == 'S'){
            System.out.printf("%.1f\n", soma);
        }else{
            System.out.printf("%.1f\n", media);
        }
    }
 
}
