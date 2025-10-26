class boxing_unboxing {
    public static void main(String[] args) {
        Integer ob1 = new Integer(123);
        Integer ob2 = new Integer("124");
        Integer ob3 = Integer.valueOf(125);
        Integer ob4 = Integer.valueOf("126");

        System.out.println("ob1: " + ob1);
        System.out.println("ob2: " + ob2);
        System.out.println("ob3: " + ob3);
        System.out.println("ob4: " + ob4);

        // Unboxing
        int a = ob1.intValue();
        String s1 = ob2.toString();

        System.out.println("a: " + a);
        System.out.println("s1: " + s1);
    }
}