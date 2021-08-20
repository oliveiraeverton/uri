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
//        printf("o valor de i é: %d \n", i);
    }
    binario[i] = 1;
    int k = i;
    printf("%d = ", somaP);
    while(k>=0){
        printf("%d", binario[k]);
        k--;
    }
//   for(k; k>=0; k--){
//        printf("%d", binario[k]);
//   }
    printf("\n");

    return 0;
}

/*printf("i = %d >>", i);
        binario[i] = maiorValor%2;
        maiorValor = maiorValor/2;
        i++;
        if(maiorValor==2){
            break;}
        printf("i = %d\n", i);
        printf("VALOR DO maiorValor %d\n", maiorValor);*/
