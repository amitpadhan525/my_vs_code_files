interface A1
{
void call1();
}
interface B extends A1
{
void display1();
}
class C implements B
{
public void call1()
 {
   System.out.println("this is A's call");
 } 
public void display1()
{
System.out.println("This is B's display");
}
}
class Inhex
{
public static void main(String[]
 args)
{
C c = new C();
c.display1();
c.call1();
}
}