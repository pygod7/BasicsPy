# LEVEL 1 – LOOP & RANGE PROBLEMS

def problem_1():
    # 1. Print numbers from 1 to 10 using `for` and `range()`.
    print('1. Print numbers from 1 to 10 using `for` and `range()`.')
    for i in range(1, 11):
        print(i)
    print()


def problem_2():
    # 2. Print numbers from 10 to 1 using `range(start, stop, step)` (only primes).
    print('2. Print prime numbers from 10 to 1 using `range(start, stop, step)`.')

    def is_prime(num):
        sqr = int(num ** 0.5)  # finding the sqr root
        for i in range(2, sqr + 1):
            if num % i == 0:
                return False
        return True

    # note: we only need to check factors up to square root to determine primality
    for i in range(10, 1, -1):
        if is_prime(i):
            print(i)
    print()


def problem_3():
    # 3. Print every 2nd number from 2 to 20.
    print('3. Print every 2nd number from 2 to 20.')
    for i in range(2, 21, 2):
        print(i)
    print()


def problem_4():
    # 4. Print all even numbers between 1 and 40 using step size in `range()`.
    print('4. Print all even numbers between 1 and 40 using step size in `range()`.')
    for i in range(2, 41, 2):
        print(i)
    print()


def problem_5():
    # 5. Print the square of each number from 1 to 10.
    print('5. Print the square of each number from 1 to 10.')
    for i in range(1, 11):
        print(i ** i)
    print()


def problem_6():
    # 6. Print each element and its index from `[10, 20, 30, 40]` using `enumerate()`.
    print('6. Print each element and its index from `[10, 20, 30, 40]` using `enumerate()`.')
    nums = [10, 20, 30, 40]
    for po, va in enumerate(nums):
        print(po, va)
    print()


def problem_7():
    # 7. Print all characters of `"Python Loops"` one by one.
    print('7. Print all characters of "Python Loops" one by one.')
    string = "Python Loops"
    for i in string:
        print(i)
    print()


def problem_8():
    # 8. Print only characters at even indices of `"Artificial Intelligence"`.
    print('8. Print only characters at even indices of "Artificial Intelligence".')
    string = "Artificial Intelligence"

    # method 1: using range
    for i in range(0, len(string), 2):
        print(string[i])

    print("--OR--")

    # method 2: using enumerate
    for ind, char in enumerate(string):
        if ind % 2 == 0:
            print(char)
    print()


def problem_9():
    # 9. Reverse a list `[2, 4, 6, 8, 10]` manually using a loop.
    print('9. Reverse a list `[2, 4, 6, 8, 10]` manually using a loop.')
    nums = [2, 4, 6, 8, 10]
    reversed_list = []

    for i in range(len(nums) - 1, -1, -1):
        reversed_list.append(nums[i])
    print(reversed_list)
    print()


def problem_10():
    # 10. Print numbers from `[1, 2, 3, 4, 5]` in reverse order using `range()`.
    print('10. Print numbers from `[1, 2, 3, 4, 5]` in reverse order using `range()`.')
    nums = [1, 2, 3, 4, 5]

    # method 1: using indices
    for i in range(len(nums) - 1, -1, -1):
        print(nums[i])

    print("--OR--")

    # method 2: using range directly
    for i in range(5, 0, -1):
        print(i)
    print()


if __name__ == "__main__":
    problem_1()
    problem_2()
    problem_3()
    problem_4()
    problem_5()
    problem_6()
    problem_7()
    problem_8()
    problem_9()
    problem_10()
