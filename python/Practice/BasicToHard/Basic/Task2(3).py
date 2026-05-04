#Input n,Print the sum of numbers from 1 to n using a loop.
n = int(input("Enter a number= "))
sum = 0
for i in range (1,n+1):
    sum = sum + i
print ("Total Sum= ",sum)
