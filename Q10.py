no=int(input("Enter the Number : "))
if(no%3==0 and no%5==0):
    print("Number is Divisible by 3 and 5")
elif(no%3==0):
    print("Number is Divisible by 3")
elif(no%5==0):
    print("Number is Divisible by 5")
else:
    print("Number is not Divisible by 3 or 5")
