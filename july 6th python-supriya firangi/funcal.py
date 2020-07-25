def Multiplication():
    a = 10
    b = 25
    Multi = a * b
    return Multi
print("After Calling the Multiplication Function: ", Multiplication())
# This function performs additiion
def add(a, b):
   return a + b
# This function performs subtraction
def subtract(a, b):
   return a - b
# This function performs division
def divide(a, b):
    return a/b
def modules(a,b):
    return a%b
def squ(a,b):
    return a**b
def exp(a,b):
    return a//b
print("Select an operation.")
print("+")
print("-")
print("/")
print("%")
print("**")
print("//")
# User input
choice = input("Enter operator to use:")
A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
if choice == '+':
   print(A,"+",B,"=", add(A,B))
elif choice == '-':
   print(A,"-",B,"=", subtract(A,B))
elif choice == '/':
   print(A,"/",B,"=", divide(A,B))
elif choice == '%':
   print(A,"%",B,"=", modules(A,B))
elif choice == '**':
   print(A,"**",B,"=", squ(A,B))
elif choice == '//':
   print(A,"//",B,"=", exp(A,B))
else:
    print("Invalid input")