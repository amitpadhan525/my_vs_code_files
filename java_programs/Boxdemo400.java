class Box {
    int length, hight, breath;

    int volume() {
        return length * hight * breath;
    }

    void settime(int l, int h, int b) {
        length = l;
        hight = h;
        breath = b;
    }
}

class Boxdemo400 {
    public static void main(String args[]) {
        Box B1 = new Box();
        Box B2 = new Box();

        B1.settime(10, 20, 30);
        B2.settime(1, 2, 3);

        int aa = B1.volume();
        int bb = B2.volume();

        System.out.println("The volume of box1 " + aa);
        System.out.println("The volume of box2 " + bb);
    }
}