a=int(input('enter number '))
x=a
rev=0
while a>0:
    rem=a%10
    rev=rem+rev*10
    a=a//10
if x==rev:
    print(f'{x} is a palindrome')
else:
    print(f'{x} not a palindrome number')