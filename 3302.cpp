#include<stdio.h>

int main(){
    
    int casoTeste, numero, i;
        i = 1;
        scanf("%d", &casoTeste);
        while(casoTeste>0){
            casoTeste--;
            scanf("%d",&numero);
            printf("resposta %d: %d\n",i ,numero);
            i++;
    
        }
    
    return 0;
}
