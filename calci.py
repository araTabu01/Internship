def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("Multiply")
print("Divide")
while True:
    choice=int(input("Enter your choice (1-4):"))
    if choice in [1,2,3,4]:
        x=float(input("Enter first number:"))
        y=float(input("Enter second number:"))
    if choice==1:
       print(add(x,y))
    elif choice==2:
        print(subtract(x,y))
    elif choice==3:
        print(multiply(x,y))
    elif choice==4:
        print(divide(x,y))
    else:
        print("Invalid choice")
        break