num1=float(input("enter the number:"))
num2=float(input("enter another number:"))
op= input("enter operation(+,-,*,/)")
if op=='+':
    print("Result=",num1+num2)
elif op=='-':
    print("Result=",num1-num2)
elif op=='*':
    print("Result=",num1*num2)
elif op=='/':
    if num2 !=0:
        print("Result=",num1/num2)
    else:
        print("cannot divided by zero")
else:
    print("invalid operation")

