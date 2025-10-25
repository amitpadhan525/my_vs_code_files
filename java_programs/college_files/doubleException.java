//this file has some error

class doubleException
{
public static void main(String args[])
{

int a=10,b=0,c,d;
System.out.println("this line will be printed");
try
{

d=Integer.parseInt("ABC");
}
try
{
c=a/b;
}

catch(ArithmeticException e)
{
System.out.println(e);
}
catch(NumberFormatException ne)
{
System.out.println(ne);
}
}
}