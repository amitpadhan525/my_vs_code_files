a =int(input('entr a number: '))
def sum_of_number(a):
    if a==0:
        return 0
    else:
        return (a%10+sum_of_number(a//10))        # 123%10=3, 123//10=12, 12%10=2, 12//10=1, 1%10=1, 1//10=0            //10 is used to remove the last digit
print(sum_of_number(a))