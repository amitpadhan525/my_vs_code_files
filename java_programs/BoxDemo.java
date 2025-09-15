class Box {
    int length;
    int width;
    int height;
}

class BoxDemo {
    public static void main(String[] args) {
        Box B1 = new Box();
        int vol1;
        B1.length = 20;
        B1.width = 40;
        B1.height = 50;

        vol1 = B1.length * B1.width * B1.height;
        System.out.println("The volume of Box1 is: " + vol1);

        Box B2 = new Box();
        B2.length = 3;
        B2.width = 4;
        B2.height = 1;

        int vol2 = B2.length * B2.width * B2.height;
        System.out.println("The volume of Box2 is: " + vol2);
    }
}
