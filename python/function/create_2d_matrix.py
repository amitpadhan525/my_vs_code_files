 
def create_2d_matrix(row,col):
    matrix=[]
    for i in range (row):
       row=[]
       for j in range (col):
           value=int(input(f'enter value for row {i+1} ::'))
           row.append(value)
       matrix.append(row)
    print('matrix is: ')
    for row in matrix:
       print(row)

row=int(input('Enter number of rows :')) 
col=int(input('Enter number of columns :'))
create_2d_matrix(row,col)