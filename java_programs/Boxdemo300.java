class Box
{

int length,hight,breath;
int volume()
{
return length*hight*breath;
}
}

class Boxdemo300
{
public static void main(String args[])

{
Box B1=new Box();
B1.length=20;
B1.hight=30;
B1.breath=40;
int kk=B1.volume();
System.out.println("The volume of Box "+kk);
}
}