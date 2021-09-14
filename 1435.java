import java.io.IOException;
import java.util.Scanner;

public class main {
 
    public static void main(String[] args) throws IOException {
 
       //CRIANDO UM OBJETO DO TIPO SCANNER
        Scanner input = new Scanner(System.in);
        

        //DECLARANDO UMA MATRIZ
        int[][] matriz;


        //DECLARANDO O TAMANHO MAXIMO DA MATRIZ
        matriz = new int[100][100];

        while(true){
            //ENTRADA PARA O TAMANHO INICIAL DA MATRIZ
            int entrada = input.nextInt();
            if(entrada == 0){break;}
            //VALOR QUE SERA ATRIBUIDO A MATRIZ
            int valor = 1;
            int variavel_linha = 0;
            int variavel_coluna = 0;
            int copia_entrada = entrada;
            //ATRIBUINDO VALORES PARA A MATRIZ[entrada][entrada]
            //
            float divisor;
            if (entrada%2 == 0){divisor = entrada / 2;}else{
                divisor = (entrada / 2)+1;
            }
            
            
            for(int k = 1; k<divisor+1 ;k++){
                for(int linha = variavel_linha; linha < copia_entrada; linha++){
                    for(int coluna = variavel_coluna; coluna< copia_entrada; coluna++){
                        
                        matriz[linha][coluna] = k;


                    }
                            
                }//FIM DO FOR COLUNA
            variavel_linha++;
            variavel_coluna++;
            copia_entrada--;
            }
        
            for (int i = 0; i < entrada; i++){
                for (int j = 0; j < entrada; j++){
                    if (j == 0)
                        System.out.printf("%3d", matriz[i][j]);
                    else
                        System.out.printf(" %3d", matriz[i][j]);
                }
                System.out.printf("\n");
            }
            System.out.printf("\n");
        }
    }
    
 
}
