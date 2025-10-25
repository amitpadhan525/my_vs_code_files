class fianallyCatchException
{
public static void main(String args[])
{

int a=10,b=0,c;
System.out.println("this line will be printed");
try
{
c=a/b;
}

catch(Exception e)
{
System.out.println(e);
}
finally
{
System.out.println("this code will be exicute");
}
//System.out.println("this code also print");
}
}
