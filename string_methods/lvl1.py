# LEVEL 1 – BASIC PROBLEMS

def problem_1():
    # 1. Reverse the string "OpenAI is amazing".
    string = "OpenAI is amazing"
    reversed_string = string[::-1]
    print('1. Reverse the string "OpenAI is amazing".')
    print("Answer:", reversed_string, "\n")


def problem_2():
    # 2. Count the number of vowels in "Artificial Intelligence rocks".
    string = 'Artificial Intelligence rocks'
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in string.lower():
        if i in vowels:
            count += 1
    print('2. Count the number of vowels in "Artificial Intelligence rocks".')
    print(f"Answer: There are {count} vowels in the given string!\n")

    # OR
    # print(f"There are {sum(char in 'aeiou' for char in string.lower())} vowels in the given string!")


def problem_3():
    # 3. Check whether "racecar" is a palindrome.
    string = "racecar"
    print('3. Check whether "racecar" is a palindrome.')
    if string == string[::-1]:  # OR ''.join(reversed(string)) == string:
        print("Answer: Palindrome!\n")
    else:
        print("Answer: Not Palindrome!\n")


def problem_4():
    # 4. Convert "python programming" to uppercase and lowercase.
    string = "python programming"
    lowercase = string.lower()
    uppercase = string.upper()
    print('4. Convert "python programming" to uppercase and lowercase.')
    print(f"Answer:\nLowercase : {lowercase}\nUppercase : {uppercase}\n")


def problem_5():
    # 5. Remove all spaces from "Data Science is fun".
    string = 'Data Science is fun'
    removed_space = string.replace(" ", "")
    print('5. Remove all spaces from "Data Science is fun".')
    print("Answer:", removed_space, "\n")


def problem_6():
    # 6. Count the number of words in "Machine learning simplifies tasks".
    string = "Machine learning simplifies tasks"
    word_count = len(string.split())
    print('6. Count the number of words in "Machine learning simplifies tasks".')
    print(f"Answer: The words count is: {word_count}\n")


def problem_7():
    # 7. Replace every occurrence of "a" with "@" in "bananas are awesome".
    string = 'bananas are awesome'
    replaced = string.replace('a', '@')  # must make a new string to define it
    print('7. Replace every occurrence of "a" with "@" in "bananas are awesome".')
    print("Answer:", replaced, "\n")


def problem_8():
    # 8. Check if "Hello World" starts with "Hello" or ends with "World".
    string = "Hello World"
    result = string.startswith("Hello") or string.endswith("World")
    print('8. Check if "Hello World" starts with "Hello" or ends with "World".')
    print("Answer:", result, "\n")


if __name__ == "__main__":
    problem_1()
    problem_2()
    problem_3()
    problem_4()
    problem_5()
    problem_6()
    problem_7()
    problem_8()
