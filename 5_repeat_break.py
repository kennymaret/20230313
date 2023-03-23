while True
#1.input

x1 = input("enter x1:")
x2 = input("enter x2:")
op = input("enter operator:")

#2.process
if op == "+":
    sum= int(x1)+int(x2)
elif op == "-":
    sum = int(x1)- int(x2)

#3.output
print(f"sum:{sum}")
res = input("continue? (Y/N)")
if res.upper()[0] == "N":
    break; 