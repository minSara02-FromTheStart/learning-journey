#Practice 3: Even or Odd
#Function is_even(n) → returns True if even, else False
#Call it for numbers 1–10 and print results.

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
for i in range(1,11):
     print(i , is_even(i))
