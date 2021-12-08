import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner input = new Scanner(System.in);
        
        int x;
        
        x = input.nextInt();
        
        if(x%2 == 0){
            x--;
        }
        for(int i = 1; i <= x; i = i + 2){
            System.out.println(""+i);
        }
    }
 
}
