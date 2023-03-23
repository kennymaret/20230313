import math

sum = 0

#1.input

x1 = input("enter x1:")
x2 = input("enter x2:")
x3 = input("enter x3:")
op = input("enter operator:")

#2.process
if op == "+":
    sum= int(x1)+int(x2)
elif op == "-":
    sum = int(x1)- int(x2)
elif op == "/":
    sum = int(x1)- int(x2)
elif op == "*":
    sum = int(x1)- int(x2)
elif op == "avg":
    sum = (int(x1)- int(x2))/2
elif op == "sd":
    average = (int(x1) + int(x2) + int(x3))/3
    step1 = int(x1) - average
    step2 = int(x2) - average
    step3 = int(x3) - average
    step4 = (step1**2) + (step2**2) + (step3**2)
    sd= math.sqrt((step4/3))
    

#3.output
if op == "+":
    print(f"sum:{sum}")
elif op == "-":
    print(f"sum:{sum}")
elif op == "/":
    print(f"sum:{sum}")
elif op == "*":
    print(f"sum:{sum}")
elif op == "avg":
    print(f"sum:{sum}")
elif op == "sd":
    print(f"sum:{sd}")
