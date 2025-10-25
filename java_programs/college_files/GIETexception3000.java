class GIETexception3000
{
public static void main(String args[])
{
System.out.println("This line will be print");
try
{
int a=Integer.parseInt("ABC");
}
catch(Exception e)
{
System.out.println(e);
System.out.println("This line will be exicuted");
}

}
}