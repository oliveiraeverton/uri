import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner input = new Scanner(System.in);
        
        int alcool=0, gasolina=0, diesel=0;
        int entrada;
        
        do{

            entrada = input.nextInt();
            
            if (entrada == 1){alcool++;}
            else if(entrada == 2){gasolina++;}
            else if(entrada == 3){diesel++;}
        } while(entrada != 4);
        
        
        System.out.println("MUITO OBRIGADO");
        System.out.println("Alcool: "+alcool);
        System.out.println("Gasolina: "+gasolina);
        System.out.println("Diesel: "+diesel);
    }
 
}
