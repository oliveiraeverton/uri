import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner input = new Scanner(System.in);
        float valor;
        float imposto, calculo, puro;
        valor = input.nextFloat();
        puro = valor;

        if (valor <= 2000.00){
            System.out.println("Isento");
        }else if(valor >= 2000.01 && valor <= 3000){
            valor = valor - 2000;
            valor = valor * 0.08f;
            System.out.printf("R$ %.2f\n", valor);

        }else if(valor >= 3000.01 && valor <= 4500){
            valor = valor - 3000.01f;
            calculo = 80.00f;
            valor = (valor * 0.18f) + calculo;
            System.out.printf("R$ %.2f\n", valor);

        }else if(valor >= 4500){
            valor = valor - 4500;
            calculo = 350.00f; 
            valor = (valor * 0.28f) + calculo;
            System.out.printf("R$ %.2f\n", valor);
        }
 
    }
 
}
