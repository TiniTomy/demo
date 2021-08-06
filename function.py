n=int(input("enter the number: "))
i=n
while n>0:
    print(" "*(i-n),end="")
    print("*"*n)
    n=n-1
    
n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",avg)


n=int(input("enter a nuumber: "))
i=n
while i>0:
    k=i
    while(n-k)>0:
        print(" ",end=" ")
        k=k+1
    for j in range(i):
        print("*",end=" ")
    print()
    i=i-1
