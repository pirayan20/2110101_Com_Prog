import java.util.Scanner;

public class Parentheses {
    public static void main(String[]args) {
        Scanner kb = new Scanner(System.in);
        String ans = "";
        String x = kb.nextLine();

        String first = "()[]";
        String second = "[]()";

        for (char e : x.toCharArray()){
            String s = String.valueOf(e);
            if (first.indexOf(s) >= 0){
                ans += second.substring(first.indexOf(s),first.indexOf(s) + 1);
            } else ans += s;
        }

        kb.close();
        System.out.println(ans);

    }
}
    
