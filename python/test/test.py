# def strip(n):
#     if n%2==1:
#         print('Weird')
#     elif n%2==0&2<=n>=5:
#         print("Not Weird")
#     elif(n%2==0&6<=n>=20):
#         print("Weird")
#     elif n%2==0&n<20:
#         print("Not Weird")
# strip(3)


# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())



# import os
# import random
# for i in range(100):
#     number=int(input("choose a number between 1 to 5 :"))
#     if number==random.randint(1,5):
#         print("you win")
#     else:
#         os.remove("/home/amit/Desktop/amit.txt")
#         print("you lost file")

# arr = [1, 2, 3]
# print('     '.join(str(i) for i in arr))




aa=input("enter name of file :")
bb=input("enter what to write :")
with open(aa,"w") as file:
    file.write(bb)


    