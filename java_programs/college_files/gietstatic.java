class Staticdemo {
    static int x = 10;
    static int b = 20;

    static void display() {
        System.out.println("The value of x is: " + x);
    }
}

class gietstatic {
    public static void main(String args[]) {
        Staticdemo.display();
        System.out.println("The value of b is: " + StaticDisplay.b);
    }
}