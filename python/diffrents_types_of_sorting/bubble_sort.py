list=[2,45,42,3,2,4,65,45]
for i in range(len(list)-1):
    for j in range(len(list)-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
                 #OR
            # temp=list[j]
            # list[j]=list[j+1]
            # list[j+1]=temp


print(list)