class GIETexception2
{
public static void main(String args[])

{
System.out.println("This line will be printed");

int a=10,b=0,c;
try 
{
c=a/b;
}
catch(Exception e)
{
System.out.println(e);
}

System.out.println("This line will be printed");
System.out.println("This line will be exicute");
}
}