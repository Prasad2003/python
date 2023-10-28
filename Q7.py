arr=[]
cnt=0
sumeven=sumodd=0
while(cnt!=10):
    arr.append(int(input("Enter Integer:")))
    cnt=cnt+1
for i in range(10):
    if(arr[i]%2==0):
        sumeven=sumeven+arr[i]
    else:
        sumodd=sumodd+arr[i]
print("Sum of Even Numbers:",sumeven)
print("Sum of Odd Numbers:",sumodd)
               
