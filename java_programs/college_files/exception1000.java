class exception1000
{
public static void main(String args[])
{
System.out.println("this line will be print");
int a=10,b=20;
try
{
int c=a/b;
System.out.println("the try block will be printed");
}

catch(Exception e)
{
System.out.println(e);
System.out.println("the catch block woll be printed");
}
System.out.println("this line will be print");
}
}