#Practice 5: Factorial
#Function factorial(n) → returns factorial of n
#Example: factorial(5) → 120

def fraction(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fraction(n-1)
 
num = int(input("enter a number = "))
print("Factorial of",num,"is ",fraction(num))
