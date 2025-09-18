class Box {
    int length;
    int width;
    int height;

    Box() {
        length = 10;
        width = 20;
        height = 30;
    }

    int volume() {
        return length * width * height;
    }
}

class Boxdemo5000 {
    public static void main(String args[]) {
        Box B1 = new Box();
        int vol = B1.volume();
        System.out.println("The value of Box is: " + vol);
        Box B2 = new Box();
        int vol2 = B2.volume();
        System.out.println("The value of Box is: " + vol2);
    }
}
