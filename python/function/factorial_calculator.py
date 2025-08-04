# def factorial(num):
#     if num==0:
#         return 0
#     else:
#         i=1
#         fact=1
#         while i<=num:
#             fact=fact*i
#             i=i+1
#         return fact


# print(factorial(int(input('enter a number'))))




                    #USING FUNCTION RECURSION


def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
    
print(factorial(int(input('enter a number :'))))
