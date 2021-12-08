#include <stdio.h>

void imprimeVetor(int vetor[5], int valor, int maximo){
    
    if(valor == 1){
        for(int k = 0; k < maximo; k++){
            printf("impar[%d] = %d\n", k, vetor[k]);
        }
    }

    if(valor == 0){
        for(int k = 0; k < maximo; k++){
            printf("par[%d] = %d\n", k, vetor[k]);
        }
    }
}
int main(){
    
    int impar[5];
    int par[5];
    int entrada;
    int valor;
    int quinze = 15;
    int i = 0;
    int p = 0;
    while(quinze > 0){
        quinze--;
        scanf("%d", &entrada);

        if(entrada%2 == 0){
            par[p] = entrada;
            p++;
            if(p == 5){
                valor = 0; // PARA PAR
                //FUNCAO
                imprimeVetor(par, valor, p);
                p = 0;
            }
        }else{
            impar[i] = entrada;
            i++;
            if(i == 5){
                valor = 1; // PARA IMPAR
                //FUNCAO
                imprimeVetor(impar, valor, i);
                i = 0;
            }
        }
    }
    //imprimir
    
    imprimeVetor(impar, 1, i);
    
    imprimeVetor(par, 0, p);


    return 0;
}
