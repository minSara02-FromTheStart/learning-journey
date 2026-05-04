#Input two integers start and end
#Print all leap years between them (inclusive).

start = int(input("Enter start year = "))
end = int(input(" Enter end year = "))

for i in range (start,end+1):
    if (i%400==0 or i%4==0 and i%100!=0):
        print(i)
