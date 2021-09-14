import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
        int n;
        Scanner input = new Scanner(System.in);
        n = input.nextInt();
        for(int i = 1; i<10000; i++){
            if(i%n==2){
            System.out.printf("%d\n",i);}
        }
    }
 
}
