import java.util.Scanner;

public class RLE {
    static String toRLE(String first){
        int i = 0;
        String ans = "";

        while (i < first.length()){
            int count = 1;
            String alpha = first.substring(i,i+1);
            int k = i;
            while (k < first.length() - 1){
                if (first.substring(k,k+1).equals(first.substring(k+1,k+2))){
                    count++;
                    k++;
                } else break;
            }
            ans = ans + alpha + " " + count + " ";
            i = k+ 1;
        }
        return ans;
    }

    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        String a = kb.nextLine();
        System.out.println(toRLE(a));
        kb.close();
    }
}

