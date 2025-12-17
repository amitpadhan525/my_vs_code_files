class Animal {
    void sound() {
        System.out.println("Animal sound");
    }
}

class Dog extends Animal {
    void sound() {
        System.out.println("Dog barks");
    }
}

public class InheritanceOverride {
    public static void main(String args[]) {
        Animal a = new Animal();
        Dog d = new Dog();
        a.sound();
        d.sound();
    }
}
