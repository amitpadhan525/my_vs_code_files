class Box{
int length,width,breath;
Box(int l,int w,int b){
length=l;
width=w;
breath=b;
}
Box(int side){
length=width=breath=side;
}
Box(){
length=width=breath=-1;
}
int volume(){
return length*width*breath;
}
}
class ConsOverload{
public static void main(String[]args){
Box B1=new Box();
Box B2=new Box(10);
Box B3=new Box(10,20,30);
System.out.println("Volume of box1: "+B1.volume());
System.out.println("Volume of box2: "+B2.volume());
System.out.println("Volume of box3: "+B3.volume());
}
}