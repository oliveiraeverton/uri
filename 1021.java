import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {

        Dinheiro dinheiro = new Dinheiro();

        //System.out.println();

        //VETOR
        int vetor[];
        vetor = new int[2];

        //RETORNA O VALOR INTEIRO
        int inteiro = dinheiro.getInteiro(); 

        //RETORNA O VALOR DECIMAL COMO INTEIRO
        int resto = dinheiro.getResto(inteiro);

        //OPERACAO CEDULAS

        vetor = dinheiro.divmod(inteiro, 100);
        int cem = vetor[0];
        vetor = dinheiro.divmod(vetor[1], 50);
        int cinquenta = vetor[0];
        vetor = dinheiro.divmod(vetor[1], 20);
        int vinte = vetor[0];
        vetor = dinheiro.divmod(vetor[1], 10);
        int dez = vetor[0];
        vetor = dinheiro.divmod(vetor[1], 5);
        int cinco = vetor[0];
        vetor = dinheiro.divmod(vetor[1], 2);
        int dois = vetor[0];
        int um = vetor[1];

        //OPERACAO MOEDA

        vetor = dinheiro.divmod(resto, 50);
        int cinqueantaCentavos = vetor[0];
        vetor = dinheiro.divmod(vetor[1], 25);
        int vinteCincoCentavos = vetor[0];
        vetor = dinheiro.divmod(vetor[1], 10);
        int dezCentavos = vetor[0];
        vetor = dinheiro.divmod(vetor[1], 5);
        int cincoCentavos = vetor[0];
        int umCentavo = vetor[1];
        
        System.out.println("NOTAS:");
        System.out.println(cem + " nota(s) de R$ 100.00");
        System.out.println(cinquenta + " nota(s) de R$ 50.00");
        System.out.println(vinte + " nota(s) de R$ 20.00");
        System.out.println(dez + " nota(s) de R$ 10.00");
        System.out.println(cinco + " nota(s) de R$ 5.00");
        System.out.println(dois + " nota(s) de R$ 2.00");
        System.out.println("MOEDAS:");
        System.out.println(um + " moeda(s) de R$ 1.00");
        System.out.println(cinqueantaCentavos + " moeda(s) de R$ 0.50");
        System.out.println(vinteCincoCentavos + " moeda(s) de R$ 0.25");
        System.out.println(dezCentavos + " moeda(s) de R$ 0.10");
        System.out.println(cincoCentavos + " moeda(s) de R$ 0.05");
        System.out.println(umCentavo + " moeda(s) de R$ 0.01");



    }//fim do main(String)
}//fim do Main
class Dinheiro{

    int inteiro;
    int resto;
    float entrada;
    Scanner input = new Scanner(System.in);

    //CONSTRUTOR
    public Dinheiro(){
        this.entrada = input.nextFloat();
    }

    public int getInteiro(){
        this.inteiro = (int) this.entrada;
        //System.out.printf("PARTE INTEIRA: %d \n",this.inteiro);
        return inteiro;
    }
    public int getResto(int inteiro){
        this.resto = (int)(this.entrada*100 - inteiro*100);
       //System.out.printf("PARTE DO RESTO: %d \n", this.resto);
        
        return resto;
    }

    public int[] divmod(int dividendo, int divisor){
        int vetor[];
        vetor = new int[2];
        if (divisor > 0){
            vetor[0] = (int) (dividendo/divisor);
            vetor[1] = (int) (dividendo - (vetor[0]*divisor)); 
            return vetor;
        }
        vetor[0] = dividendo;
        vetor[1] = 0;
        return vetor;
    }
    

}



