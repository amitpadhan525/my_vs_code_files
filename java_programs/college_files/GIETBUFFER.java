//use buffer reader class to the input
import java.io.*;
class GIETBUFFER
{
public static void main(String args[])throws IOException
{
InputStreamReader ir=new InputStreamReader(System.in);
BufferedReader bb=new BufferedReader(ir);
System.out.println("Enter your name :");
String nm=bb.readLine();
System.out.println("My name is "+nm); 


}
}