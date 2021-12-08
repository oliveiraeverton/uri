import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
    Scanner input = new Scanner(System.in); int x, y;
    int soma=0;
    x = input.nextInt(); y = input.nextInt();
    if(x>y){
        int aux;
        aux = x;
        x = y;
        y = aux;
    }
    while(x<=y){
        if(x%13 != 0){
            soma += x;
        }
        x++;
    }
    System.out.println(""+soma);
    }
 
}
