#Input an integer n
#Print its reverse using loops and conditions.

n = int(input("Enter a number= "))
print (" n = ", n)
rev = 0
while n>0:
    digit = n%10                          #We extract the last digit
    rev = rev * 10 + digit                #We build the reverse number
    n = n//10                             #We remove the last digit from n
print ("reverse = " , rev)
