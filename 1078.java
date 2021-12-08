import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner input = new Scanner(System.in);
        int n;
        n = input.nextInt();
        int i = 1;
	int j = 10;
        while(j> 0){
            System.out.printf("%d x %d = %d\n",i, n, i*n);
            i++;
            j--;
        }
        
 
    }
 
}
