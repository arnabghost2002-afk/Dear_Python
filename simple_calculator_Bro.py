#Python calculator


operator= input("Enter Operators (+ - * /): ")
num1= float(input("Enter NUM1= "))
num2= float(input("Enter NUM2= "))


if operator=="+":
    result=num1+num2
    print(result)
elif operator=="-":
    result=num1-num2
    print(result)
elif operator=="*":
    result=num1*num2
    print(result)
elif operator=="/":
    result=num1/num2
    print(result)
else:
    print("Invalid operator")
