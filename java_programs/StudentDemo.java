class Student
{
 String name;
 int age;
 int rollNo;

 Student(String n, int a, int r)
 {
   name = n;
   age = a;
   rollNo = r;
 }
 void display() {
   System.out.println("Name: " + name);
   System.out.println("Age: " + age);
   System.out.println("Roll No: " + rollNo);
   System.out.println("####################");
 }
}
public class StudentDemo 
{
 public static void main(String args[])
 {
   Student s1 = new Student("Ayush", 19, 101);
   Student s2 = new Student("Amit", 19, 102);
   Student s3 = new Student("Anurag", 20, 103);
   Student s4 = new Student("Badal", 18, 104);

   s1.display();
   s2.display();
   s3.display();
   s4.display();
    }
}