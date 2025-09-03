bin=input("Enter binary number :")
l=len(bin)
dec=0
for i in bin:
    i=int(i)
    dec=dec+(i*(2**(l-1)))
    l=l-1
print(dec)