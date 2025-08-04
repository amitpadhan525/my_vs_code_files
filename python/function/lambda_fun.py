a=int(input("enter 1st no, :"))
b=int(input("enter 2nd no. :"))


add=lambda x,y:x+y
sub=lambda x,y:x-y
mul=lambda x,y:x*y
div=lambda x,y:x/y
mod=lambda x,y:x%y

print(a,"+",b,"=",add(a,b))
print(a,"-",b,"=",sub(a,b))
print(a,"*",b,"=",mul(a,b))
print(a,"/",b,"=",div(a,b))
print(a,"%",b,"=",mod(a,b))
