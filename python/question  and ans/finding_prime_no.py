def prime(n):
    count=0
    print("|| PRIME NUMBERS ARE ||")
    for i in range(n+1):
        is_prime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            if i>1:
                print(i)
                count=count+1
    print('total prime no. ',count)

a=int(input("range 1 to "))
prime(a)