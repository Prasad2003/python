
no=int(input("Enter Number= "))

sum=0
while(no!=0):
    rem=no%10
    sum=sum+int(rem)
    no=no/10
print("Sum of Digits : ",int(sum))
