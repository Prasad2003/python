cnt=0
arr=[]
while(cnt!=10):
    arr.append(int(input("Enter Integer:")))
    cnt=cnt+1

arr.sort()
flag=0
for i in range(9):
    if(arr[i]==arr[i+1]):
        print("DUPLICATES",arr[i])
        flag=1
if(flag==0):
    print("ALL UNIQUE")
       
