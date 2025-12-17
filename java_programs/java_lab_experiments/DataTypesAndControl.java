public class DataTypesAndControl {
    public static void main(String args[]) {
        int a = 10;
        double d = 20.5;
        char c = 'A';
        boolean b = true;

        double sum = a + d;
        System.out.println("Sum: " + sum);

        int arr[] = {1, 2, 3, 4, 5};
        System.out.println("Element at index 2: " + arr[2]);

        if (b) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }

        for (int i = 0; i < 5; i++) {
            System.out.println(arr[i]);
        }
    }
}
