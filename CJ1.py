def trace(matrix,n):
    sum=0
    for i in range(n):
        sum+=matrix[i][i]
    return sum        

def checkduplicate(l):
    if len(l)==len(set(l)):
        return False
    else:
        return True
def countrows(matrix,n):
    count=0
    a=0
    for i in range(n):
        a=checkduplicate(matrix[i])
        if a:
            count=count+1
    return count
def countcols(matrix,n):
    count=0
    a=0
    for i in range(n):
        a=[sub[i] for sub in matrix]
        if checkduplicate(a):
            count=count+1
    return count


s=0 
x=1
n = int(input("Enter N:"))
matrix=[]
for i in range(n):
    a=[]
    for j in range(100):
        if len(a)==n:
            break
        s=int(input(""))
        if(s>n):
            print("Invalid input:")
            continue
        a.append(s)
    matrix.append(a)
#print(matrix)
print("case #",x,":",end=" ")
print(trace(matrix,n),end=" ")
print(countrows(matrix,n),end=" ")
print(countcols(matrix,n))