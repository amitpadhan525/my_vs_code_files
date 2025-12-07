def fact(a):
    if a==0:
        return 1
    return a*fact(a-1)
        

print(fact(int(input("enter number to calculate factorial :"))))