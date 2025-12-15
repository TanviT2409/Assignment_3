def Factorial(x):
    fact= 1
    for i in range (1,x+1):
        fact = fact *i
    return fact

x= int(input("Enter a number: "))
print(f"Factorial of {x} is: {Factorial(x)}")