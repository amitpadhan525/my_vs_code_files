number=int(input("Enter number :"))
bin=[]
if number==0:
    bin=[0]
else:
    while number>0:
        if number%2==1:
            bin.insert(0,1)
        else:
            bin.insert(0,0)
        number=number//2
print(bin)