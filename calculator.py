print("Hello,How Can Help You Today ?")
print("\n WELCOME TO CALCULATOR! \n")

x=int(input("Enter first number-"))
y=input("enter a operator(+,-,*,/,%)")
z=int(input("Enter second number-"))
if y=="+":
    print("Your Addition Is:",x+z)
elif y=="-":
    print("Your Substraction Is:",x-z)
elif y=="*":
    print("Your Multiplication Is:",x*z)
elif y=="/":
    print("Your Division Is:",x/z)
elif y=="%*100":
    print("Your Modules Is:",x/z*100)
else:
    print("You Entered A Wrong Operator")
print("\n Thankyou For Using Calculator \n")