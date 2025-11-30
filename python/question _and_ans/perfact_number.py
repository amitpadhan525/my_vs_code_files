# a=int(input("enter : "))
# sum=0
# for i in range(1,a):
#     if a%i==0:
#         sum=sum+i

# if sum==a:
#     print("perfact number")



def is_perfact(number):
    if number==0:           # 0 is not PERFACT number
        return 0
    sum=0
    for i in range(1,number):
        if number%i==0:
            sum+=i
    
    if sum==number:
        return 1
    else:
        return 0


for i in range(1000):
    if is_perfact(i):
        print(f"{i} PERFACT")
