import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int doit = sc.nextInt();
        int mnem = doit;
        int summ = doit;
        int tseloe = 0;
        int ostatok = 0;
        while (3 <= mnem) {
            tseloe += mnem / 3;
            ostatok += mnem % 3;
            if (ostatok >= 9) {
                tseloe += 4;
                ostatok = ostatok % 3;
            }
            mnem /= 3;
        }
        summ += tseloe + (ostatok / 3);
        System.out.println(doit + " = " + summ);
    }
}
