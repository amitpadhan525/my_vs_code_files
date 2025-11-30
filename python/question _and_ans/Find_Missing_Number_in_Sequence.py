sec=[1,2,3,4,5,7,8,9,10]
print(sec)
print('MISSING NUMBER ::')
for i in range (len(sec)):
    if sec[i]!=i+1:
        print(i+1)
        break