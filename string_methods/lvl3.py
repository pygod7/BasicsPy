# LEVEL 3 – ADVANCED STRING PROBLEMS

def problem_21():
    # 21. Find the longest word in "Deep learning simplifies many complex tasks".
    string = "Deep learning simplifies many complex tasks"

    words = string.split(" ")
    greatest = words[0]
    for i in range(len(words)):
        if len(words[i]) > len(greatest):
            greatest = words[i]

    print("21. The longest word is {}".format(greatest), "\n")


def problem_22():
    # 22. Count uppercase and lowercase letters in "OpenAI GPT Model".
    string = "OpenAI GPT Model"
    ucase = 0
    lcase = 0
    for i in string:
        if i.isupper():
            ucase += 1
        elif i.islower():
            lcase += 1
    print("22. Ucase : {}, Lcase = {}".format(ucase, lcase), "\n")


def problem_23():
    # 23. Check if "listen" and "silent" are anagrams.
    one = "listen"
    two = "silent"

    count1 = {}
    count2 = {}

    for i in one:
        count1[i] = count1.get(i, 0) + 1
    for i in two:
        count2[i] = count2.get(i, 0) + 1

    is_anagram = True
    for i in count1:
        if i not in count2 or count1[i] != count2[i]:
            is_anagram = False
            break

    if is_anagram and len(count1) == len(count2):
        print("23. Anagram!\n")
    else:
        print("23. Not an anagram\n")


def problem_24():
    # 24. Remove all duplicate characters from "programming".
    string = "programming"
    result = ''
    for ch in string:
        if ch not in result:
            result += ch
    print("24. Remove duplicates:", result, "\n")


def problem_25():
    # 25. Find the most frequent character in "data science is fun".
    string = "data science is fun"
    count = {}

    for i in string:
        if i != " ":
            count[i] = count.get(i, 0) + 1

    # find the most frequent character in one pass
    biggest = 0
    key = ''
    for k, v in count.items():
        if v > biggest:
            biggest = v
            key = k

    print("25. The most frequent character is:", key, "\n")


def problem_26():
    # 26. Check if "_variable123" is a valid Python identifier.
    string = "_variable123"
    print("26. Is valid identifier?:", string.isidentifier(), "\n")


if __name__ == "__main__":
    problem_21()
    problem_22()
    problem_23()
    problem_24()
    problem_25()
    problem_26()
