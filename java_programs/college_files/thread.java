// use of thread
//thread is a class of lang pkg not required for import


class thread
{
public static void main(String args[])

{
Thread t=Thread.currentThread();     // currentThread is static because call by class

System.out.println("currentThread "+t);

t.setName("myThread");              //setName is non static because call by object

System.out.println("after change "+t);

try
{
for(int i =5;i>0;i--)
{
System.out.println(i);
Thread.sleep(1500);
}
}

catch(InterruptedException e) 
{
    System.out.println(e);
}

}
}