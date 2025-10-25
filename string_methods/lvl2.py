# LEVEL 2 – INDEXING, SLICING, AND MANIPULATION

def problem_9():
    ## 9. Print every second character of "Programming is fun".
    string = "Programming is fun"
    print('9. Print every second character of "Programming is fun".')
    print("Answer:", string[::2], "\n")


def problem_10():
    # 10. Extract the substring from 3rd to 8th character of "NeuralNetworks".
    string = "NeuralNetworks"
    #extracted = string[3:8] # this was mistake, it shall be 2:7 beacuase we want 3rd to 8th char seen.
    extracted = string[2:8]
    print('10. Extract the substring from 3rd to 8th character of "NeuralNetworks".')
    print("Answer:", extracted, "\n")


def problem_11():
    # 11. Reverse each word in "Deep learning models" but keep word order.
    string = "Deep learning models"
    fixed_list = []

    for i in string.split(" "):
        reverse = ''.join(reversed(i))
        fixed_list.append(reverse)

    answer = " ".join(fixed_list)

    print('11. Reverse each word in "Deep learning models" but keep word order.')
    print("Answer:", answer, "\n")

    # OR
    # print(" ".join(''.join(reversed(i)) for i in string.split(" ")))


def problem_12():
    # 12. Print all characters at even indices in "Artificial Intelligence".
    string = "Artificial Intelligence"
    print('12. Print all characters at even indices in "Artificial Intelligence".')
    print("Answer:", string[::2], "\n")

    # OR
    # for i in range(0, len(string), 2):
    #     print(string[i], end='')


def problem_13():
    # 13. Swap the first and last characters of "Python".
    string = "Python"
    swapped = string[-1] + string[1:-1] + string[0]
    print('13. Swap the first and last characters of "Python".')
    print("Answer:", swapped, "\n")


def problem_14():
    # 14. Remove the first and last character of "DataScience".
    string = "DataScience"
    removed = string[1:-1]  # or string[1:len(string)-1]
    print('14. Remove the first and last character of "DataScience".')
    print("Answer:", removed, "\n")


def problem_15():
    # 15. Count occurrences of "python" in "Python is fun. I love python!" ignoring case.
    string = "Python is fun. I love python!"
    count = sum(word.strip(".!,?") == "python" for word in string.lower().split())
    print('15. Count occurrences of "python" in "Python is fun. I love python!" ignoring case.')
    print("Answer:", count, "\n")

    # OR
    # count = 0
    # words = string.lower().split()
    # for word in words:
    #     if word.strip(".!?,") == "python":
    #         count += 1
    # print(count)


def problem_16():
    # 16. Capitalize the first letter of each word in "natural language processing".
    string = "natural language processing"
    capitalized = string.title()  # each first word = capital
    print('16. Capitalize the first letter of each word in "natural language processing".')
    print("Answer:", capitalized, "\n")


def problem_17():
    # 17. Strip leading and trailing spaces from "   Hello AI   ".
    string = "   Hello AI   "
    stripped = string.strip()  # strip removes all, lstrip() removes left, rstrip() removes right
    print('17. Strip leading and trailing spaces from "   Hello AI   ".')
    print("Answer:", stripped, "\n")


def problem_18():
    # 18. Check if "123456" contains only digits.
    string = "123456"
    print('18. Check if "123456" contains only digits.')
    print("Answer:", string.isdigit(), "\n")


def problem_19():
    # 19. Join ["deep", "learning", "rocks"] into a single string separated by "-".
    list_ = ["deep", "learning", "rocks"]
    joined = '-'.join(list_)
    print('19. Join ["deep", "learning", "rocks"] into a single string separated by "-".')
    print("Answer:", joined, "\n")


def problem_20():
    # 20. Split "apple, banana , cherry, date" by commas and remove extra spaces.
    string = "apple, banana, cherry, date"
    splitted = string.split(",")
    stripped = [i.strip() for i in splitted]
    print('20. Split "apple, banana , cherry, date" by commas and remove extra spaces.')
    print("Answer:", stripped, "\n")


if __name__ == "__main__":
    problem_9()
    problem_10()
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
