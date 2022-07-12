#include <stdio.h>

int main(){

    int matriz[4][7], soma=0, maiorValor=0;
    int somaP;
    int binario[50];
    for(int i = 0; i<4; i++){
        for(int j = 0; j < 7; j++){
            scanf("%d", &matriz[i][j]);
            soma = soma + matriz[i][j];
        }
        if(soma>maiorValor){
            maiorValor = soma;
            somaP = soma;
        }
        soma = 0;
    }
    int i = 0;
    while(maiorValor!=1){
        binario[i] = maiorValor%2;
        maiorValor = maiorValor/2;
        i++;
    }
    binario[i] = 1;
    int k = i;
    printf("%d = ", somaP);
    while(k>=0){
        printf("%d", binario[k]);
        k--;
    }

    printf("\n");

    return 0;
}
