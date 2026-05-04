#Practice 4: Max of Three
#Function max_of_three(a, b, c) → returns the largest number
#Test it with random numbers.
def max_of_three(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
a = (int(input("Enter first number= ")))
print(" a = ", a)
b = (int(input("Enter second number= ")))
print(" b = ", b)
c = (int(input("Enter third number= ")))
print(" c = ", c)
print("Largest number is = ", max_of_three(a,b,c))
