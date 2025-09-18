class Box {
    double length;
    double width;
    double height;

    Box(double length, double width, double height) {
        this.length = length;
        this.width = width;
        this.height = height;
    }

    double volume() {
        return length * width * height;
    }
}

class Boxdemo10000 {
    public static void main(String args[]) {
        Box B1 = new Box(10, 20, 3);
        double vol1 = B1.volume();
        System.out.println("The value of Box is: " + vol1);

    }
}
