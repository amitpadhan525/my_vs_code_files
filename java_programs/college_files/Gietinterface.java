interface A
{
    void call();
}
interface B
{
    void show();
}

interface C
{
    void disply();
}

class D implements A,B,C
{
public void call()
{
        System.out.println("please call A");

}
public void show()
{
    System.out.println("the Bs show");
}
public void disply()
{
    System.out.println("the Cs display");
}

}



class Gietinterface
{
    public static void main(String[] args) {
        D d=new D();
        d.show();
        d.call();
        d.disply();
        
    }
}