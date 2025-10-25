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


def problem_27():
    # 27. Replace every second vowel in "Artificial Intelligence" with "*"
    string = "Artificial Intelligence"
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_string = ""
    count = 0

    for ch in string:
        if ch.lower() in vowels:
            count += 1
            if count % 2 == 0:
                new_string += "*"
            else:
                new_string += ch
        else:
            new_string += ch

    print("27.", new_string, "\n")


def problem_28():
    # 28. Reverse the order of words in "Machine learning is amazing"
    string = "Machine learning is amazing"
    words = string.split()

    reversed_words = words[::-1]
    print("28. Using slicing:", " ".join(reversed_words))

    reversed_loop = []
    for i in range(len(words)-1, -1, -1):
        reversed_loop.append(words[i])
    print("28. Using loop:", " ".join(reversed_loop), "\n")


def problem_29():
    # 29. Convert "thisIsCamelCase" to snake_case
    string = "thisIsCamelCase"
    words = []
    word = ''
    for i in string:
        if i.isupper():
            words.append(word)
            word = i.lower()
        else:
            word += i
    words.append(word)
    snake_case = "_".join(words)
    print("29.", snake_case, "\n")


def problem_30():
    # 30. Count punctuation marks in "Hello, world! How are you doing?" (original commented method)
    import string
    anotherstring = "Hello, world! How are you doing?"
    count = 0
    for i in anotherstring:
        if i in string.punctuation:
            count += 1
    print("30. Punctuation count:", count, "\n")


def problem_31():
    # 31. Compress "aaabbcaaa" to "a3b2c1"
    string = "aaabbcaaa"
    count = 1
    compressed = ""

    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            compressed += string[i-1] + str(count)
            count = 1
    compressed += string[-1] + str(count)

    print("31.", compressed, "\n")


def problem_32():
    # 32. Expand "a3b2c1" to "aaabbc"
    string = "a3b2c1"
    expaneded = ""
    for i in range(0, len(string)):
        if string[i].isdigit():
            count = int(string[i])
            letter = string[i-1]
            for j in range(int(count)):
                expaneded += letter
    print("32.", expaneded, "\n")


def problem_33():
    # 33. Check if "Machine Learning" contains only alphabets and spaces
    string = "Machine Learning"
    if " " in string:
        string = string.replace(" ", "")
        if string.isalpha():
            print("33. True\n")
        else:
            print("33. False\n")
    else:
        print("33. False\n")


def problem_34():
    # 34. Remove all digits from "AI2025 is the future 123"
    string = "AI2025 is the future 123"
    for i in string:
        if i.isdigit():
            string = string.replace(i, '')
    print("34.", string, "\n")


def problem_35():
    # 35. Mask all letters except first and last in each word of "Artificial Intelligence Rocks"
    string = "Artificial Intelligence Rocks"
    words = string.split(" ")

    # Original method (mine brain technique to solve this qn)
    masked_list = []
    for i in words:
        masked_string = ""
        first_letter = i[0]
        last_letter = i[-1]
        masked_string += first_letter
        for j in range(1, len(i)-1):
            masked_string += "*"
        masked_string += last_letter
        masked_list.append(masked_string)

    masked_string = " ".join(masked_list)
    print("35. Original method:", masked_string)

    # OR: Using generator/list comprehension  (best way, learned later.)
    masked_string_gen = " ".join(
        word[0] + "*" * (len(word)-2) + word[-1] if len(word) > 2 else word
        for word in words
    )
    print("35. Generator method:", masked_string_gen, "\n")

if __name__ == "__main__":
    problem_21()
    problem_22()
    problem_23()
    problem_24()
    problem_25()
    problem_26()
    problem_27()
    problem_28()
    problem_29()
    problem_30()
    problem_31()
    problem_32()
    problem_33()
    problem_34()
    problem_35()


#$ ggs! you've learned string methods completely! ~ Rubin B