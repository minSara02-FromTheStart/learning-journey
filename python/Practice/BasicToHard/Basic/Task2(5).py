#Count how many even numbers exist between 1 and n (inclusive).
n = int(input("enter a number= "))
count = 0
for i in range (1,n+1):
    if i%2==0:
        count += 1
print ("Total even numbers = ", count)
