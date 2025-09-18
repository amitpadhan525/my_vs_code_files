class A {
    void call() {
        System.out.println("A's method call");
    }
}

class B extends A {
    void call() {
        System.out.println("B's method is call");
    }
}

class gietoverload {
    public static void main(String args[]) {
        B bb = new B();
        bb.call();
    }
}