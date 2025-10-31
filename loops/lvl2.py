#11. Print numbers from 1–15 but skip 5 using `continue`.

"""for i in range(1, 16):
    if i==5:
        continue
    print(i)"""
    
#12. Print numbers from 1–10 but stop when 7 is reached using `break`.

"""for i in range(1, 11):
    if i==7:
        break
    print(i)
"""

#13. Use `for...else` to print `"Loop completed"` after finishing.

"""for i in range(5):
    pass
else:
    print("Loop completed!")"""


#14. Count even and odd numbers in `[3, 6, 9, 12, 15, 18]`.

"""nums = [3, 6, 9, 12, 15, 18]
e = 0
o = 0

for i in nums:
    if i%2==0:
        e+=1
    else:
        o+=1

print("Even : ", e)
print("Odd : ", o)"""

#15. From `"AI2025@OpenAI"`, count digits, alphabets, and symbols using loops.
"""import string
alpha = 0
digit = 0
symbols = 0
stringg = "AI2025@OpenAI"
for i in stringg:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        alpha+=1
    elif i in string.punctuation:
        symbols+=1

print("Digits : {} Symbols {} Alpha {}".format(digit,symbols,alpha))
"""

"""#16. Count how many times `"a"` appears in `"bananas"` without using `count()`.

string = "bananas"
c=0
for i in string:
    if str(i) == "a":
        c+=1

print("A times {}".format(c))"""

"""
#17. Print `"Fizz"` for multiples of 3, `"Buzz"` for multiples of 5, and `"FizzBuzz"` for both (1–30).

for i in range(1, 31):
    if (i%3 == 0 and i%5 == 0):
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif (i%3 == 0):
        print("Fizz")
"""


"""#18. Print all numbers between 1–50 divisible by 3 or 5 but not both.

for i in range(1, 51):
    if (i%3 == 0 and i%5 == 0):
        pass
    elif i%3==0:
        print(i)
    elif i%5==0:
        print(i)
"""
"""#19. Reverse the string `"Machine Learning"` using loops only.

string = "Machine Learning"

splitted = string.split(" ")
reversed = []
for i in range(len(splitted)-1, -1, -1):
    reversed.append(splitted[i])

print(" ".join(reversed))   #reversing the words btw.

string = "Machine Learning"  #reversing words also!

for i in range(len(string)-1, -1, -1):
    print(string[i], end="")"""