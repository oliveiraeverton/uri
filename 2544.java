import java.io.IOException;
import java.util.Scanner;
import java.io.*;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scan = new Scanner(System.in);
        //BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (scan.hasNext()){

            int kageBunshin;
            int divisores = 0;
            kageBunshin = scan.nextInt();
        
            if(kageBunshin == 1){
                System.out.println("0");
            }else{
                while(kageBunshin != 1){
                    if(kageBunshin%2==0){
                        divisores++;
                    }
                    kageBunshin /= 2;
                }
                System.out.println(divisores);
            }
            
        }
 
    }
 
}
