#Practice 7: Simple Calculator 
def cal(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b
    elif op == '%':
        return a%b
    else:
        return "invalid"
x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
op = input("Enter operator (+,-,*,/,%)")
print("x = ",x,"y = ",y,"op = ",op)
print(cal(x,y,op))         
