
#   # 0  1  1  2  3  5  8  13  21
a=[0,1]
for i in range(int(input("Enter how many fibonacci number disply : "))):
    a.append(a[len(a)-2]+a[len(a)-1])


print(a)

