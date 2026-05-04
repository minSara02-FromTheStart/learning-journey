#Practice 6: Celsius to Fahrenheit
#Function c_to_f(c) → converts Celsius to Fahrenheit
#Test for 0°C, 25°C, 100°C

def temp(c):
    f = (c*9/5) + 32
    return f
x = float(input("enter temp in celsius = "))

print("temp in celsius = ", x)
print("temp in farhrenheit = ", temp(x))
