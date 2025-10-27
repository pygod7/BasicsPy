#1. Print numbers from 1 to 10 using `for` and `range()`.

"""for i in range(1, 11):
    print(i)
"""
#2. Print numbers from 10 to 1 using `range(start, stop, step)`.

"""def is_prime(num):
    sqr = int(num ** 0.5) #finding the sqr root.
    for i in range(2, sqr+1):
        if num%i == 0:
            return False
    return True

#note : we dont need to check all factors, only checking up to its sqr root is enough to check prime.


for i in range(10, 1, -1):
    if is_prime(i):
        print(i)
    else:
        pass
"""

"""#3. Print every 2nd number from 2 to 20.

for i in range(2,21, 2):
    print(i)"""

"""#4. Print all even numbers between 1 and 40 using step size in `range()`.

for i in range(2, 41, 2):
    print(i)"""

"""#5. Print the square of each number from 1 to 10.

for i in range(1, 11):
    print(i**i)"""

#6. Print each element and its index from `[10, 20, 30, 40]` using `enumerate()`.

nums = [10, 20, 30, 40]
for po, va in enumerate(nums):
    print(po, va)
