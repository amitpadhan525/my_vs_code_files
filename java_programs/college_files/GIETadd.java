import java.io.*;
class GIETadd
{
public static void main(String args[])throws IOException
{
int a,b,sum;
InputStreamReader ir=new InputStreamReader(System.in);
BufferedReader bk=new BufferedReader(ir);

System.out.println("Enter first number :");
a=Integer.parseInt(bk.readLine());
System.out.println("Enter second number :");
b=Integer.parseInt(bk.readLine());
sum=a+b;
System.out.println("The addition is "+sum);
}
}