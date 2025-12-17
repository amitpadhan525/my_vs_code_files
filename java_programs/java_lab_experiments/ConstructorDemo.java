class Student {
    String name;
    int id;

    Student() {
        name = "Unknown";
        id = 0;
        System.out.println("Default Constructor");
    }

    Student(String n, int i) {
        name = n;
        id = i;
        System.out.println("Parameterized Constructor");
    }

    void show() {
        System.out.println(name + " " + id);
    }
}

public class ConstructorDemo {
    public static void main(String args[]) {
        Student s1 = new Student();
        s1.show();

        Student s2 = new Student("Amit", 101);
        s2.show();
    }
}
