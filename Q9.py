num=int(input("Enter number of rows : "))
no=1
for i in range(num,0,-1):
    for j in range(i):
        print(no,end=" ")
        no=no+1
    no=1
    print()
