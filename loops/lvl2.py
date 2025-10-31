# LEVEL 2 – LOOP & RANGE PROBLEMS

def problem_11():
    # 11. Print numbers from 1–15 but skip 5 using `continue`.
    print('11. Print numbers from 1–15 but skip 5 using `continue`.')
    for i in range(1, 16):
        if i == 5:
            continue
        print(i)
    print()


def problem_12():
    # 12. Print numbers from 1–10 but stop when 7 is reached using `break`.
    print('12. Print numbers from 1–10 but stop when 7 is reached using `break`.')
    for i in range(1, 11):
        if i == 7:
            break
        print(i)
    print()


def problem_13():
    # 13. Use `for...else` to print "Loop completed" after finishing.
    print('13. Use `for...else` to print "Loop completed" after finishing.')
    for i in range(5):
        pass
    else:
        print("Loop completed!")
    print()


def problem_14():
    # 14. Count even and odd numbers in [3, 6, 9, 12, 15, 18].
    print('14. Count even and odd numbers in [3, 6, 9, 12, 15, 18].')
    nums = [3, 6, 9, 12, 15, 18]
    e = 0
    o = 0
    for i in nums:
        if i % 2 == 0:
            e += 1
        else:
            o += 1
    print("Even :", e)
    print("Odd :", o)
    print()


def problem_15():
    # 15. From "AI2025@OpenAI", count digits, alphabets, and symbols using loops.
    print('15. From "AI2025@OpenAI", count digits, alphabets, and symbols using loops.')
    import string
    alpha = 0
    digit = 0
    symbols = 0
    stringg = "AI2025@OpenAI"
    for i in stringg:
        if i.isdigit():
            digit += 1
        elif i.isalpha():
            alpha += 1
        elif i in string.punctuation:
            symbols += 1
    print("Digits : {} Symbols {} Alpha {}".format(digit, symbols, alpha))
    print()


def problem_16():
    # 16. Count how many times "a" appears in "bananas" without using count().
    print('16. Count how many times "a" appears in "bananas" without using count().')
    stringg = "bananas"
    c = 0
    for i in stringg:
        if i == "a":
            c += 1
    print("A times {}".format(c))
    print()


def problem_17():
    # 17. Print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for both (1–30).
    print('17. Print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for both (1–30).')
    for i in range(1, 31):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
    print()


def problem_18():
    # 18. Print all numbers between 1–50 divisible by 3 or 5 but not both.
    print('18. Print all numbers between 1–50 divisible by 3 or 5 but not both.')
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            continue
        elif i % 3 == 0:
            print(i)
        elif i % 5 == 0:
            print(i)
    print()


def problem_19():
    # 19. Reverse the string "Machine Learning" using loops only.
    print('19. Reverse the string "Machine Learning" using loops only.')

    # reversing words
    stringg = "Machine Learning"
    splitted = stringg.split(" ")
    reversed_words = []
    for i in range(len(splitted) - 1, -1, -1):
        reversed_words.append(splitted[i])
    print(" ".join(reversed_words))

    # reversing characters
    stringg = "Machine Learning"
    for i in range(len(stringg) - 1, -1, -1):
        print(stringg[i], end="")
    print("\n")


def problem_20():
    # 20. Print all numbers from 1–10 using a `while` loop.
    print('20. Print all numbers from 1–10 using a `while` loop.')
    i = 1
    while i <= 10:
        print(i)
        i += 1
    print()


if __name__ == "__main__":
    problem_11()
    problem_12()
    problem_13()
    problem_14()
    problem_15()
    problem_16()
    problem_17()
    problem_18()
    problem_19()
    problem_20()
