# ?Create a class Student with a constructor that initializes name and roll_number. Create an object and print its attributes.
class student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def show(self):
        print(f'name={self.name} \nroll_no={self.roll_no}')
a=student('amit',10)
a.show()