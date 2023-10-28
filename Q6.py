def isprime(n):
    if(n==1 or n==0):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

N=int(input("Enter the Number to find Prime Number : "))
for i in range(N):
    if(isprime(i)):
        print(i,end=" ")
