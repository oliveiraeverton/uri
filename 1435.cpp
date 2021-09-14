#include <stdio.h>
#include<stdlib.h>

int main(){

    //declarando a matriz
    int matriz[100][100];

    while (true){
        int entrada;
        scanf("%d", &entrada);
        //ENQUANTO ENTRADA NAO FOR 0 O SCRIPT IRA RODAR
        if(entrada == 0){
            break;
        }
         int valor = 1;
         int variavel_coluna = 0;
         int variavel_linha = 0;
         int copia_entrada;
         copia_entrada = entrada;

         float divisor;

         if(entrada % 2 == 0){
             divisor = entrada / 2;
         }else{
             divisor = (entrada/2)+1;
         }

         for (int k = 1; k<divisor+1; k++){
             for(int linha = variavel_linha; linha < copia_entrada; linha++){
                 for(int coluna = variavel_coluna; coluna < copia_entrada; coluna++){

                     matriz[linha][coluna] = k;
                 }
             }
             variavel_linha++;
             variavel_coluna++;
             copia_entrada--;
        }

        for(int i = 0; i < entrada; i++){
            for(int j = 0; j < entrada; j++){
                if(j == 0){
                    printf("%3d", matriz[i][j]);
                }else{
                    printf(" %3d", matriz[i][j]);
                }
            }
            printf("\n");
        }
        printf("\n");

    }

    return 0;
}
