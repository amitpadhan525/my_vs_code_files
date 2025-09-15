import java.util.Scanner;

class gietscanner {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter 5 numbers:");

        System.out.print("Number 1: ");
        int n1 = sc.nextInt();

        System.out.print("Number 2: ");
        int n2 = sc.nextInt();

        System.out.print("Number 3: ");
        int n3 = sc.nextInt();

        System.out.print("Number 4: ");
        int n4 = sc.nextInt();

        System.out.print("Number 5: ");
        int n5 = sc.nextInt();

        int sum = n1 + n2 + n3 + n4 + n5;
        double avg = (double) sum / 5;

        System.out.println("Sum of numbers = " + sum);
        System.out.println("Average of numbers = " + avg);

        sc.close();
    }
}