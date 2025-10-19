# 21. Find the longest word in "Deep learning simplifies many complex tasks".

'''
string = "Deep learning simplifies many complex tasks"

words = string.split(" ")
global greatest

greatest = words[0]
for i  in range(len(words)):
    if len(words[i]) > len(greatest):
        greatest = words[i]

print("The longest word is {}".format(greatest))    #$ all good!
'''

## 22. Count uppercase and lowercase letters in "OpenAI GPT Model".

'''
string = "OpenAI GPT Model"
ucase = 0
lcase = 0
for i in string:
    if i.isupper():
        ucase+=1
    elif i.islower():
        lcase+=1

print("Ucase : {}, Lcase = {}".format(ucase,lcase)) #$all good
'''




# 23. Check if "listen" and "silent" are anagrams.


# 23. Check if "listen" and "silent" are anagrams

'''
one = "listen"
two = "silent"

count1 = dict()
count2 = dict()


for i in one:
    if i in count1:
        count1[i] += 1
    else:
        count1[i] = 1


for i in two:
    if i in count2:
        count2[i] += 1
    else:
        count2[i] = 1

is_anagram = True
for i in count1:
    if i not in count2 or count1[i] != count2[i]:
        is_anagram = False
        break


if is_anagram and len(count1) == len(count2):
    print("Anagram!")
else:
    print("Not an anagram")

     
    #basically comparing keys. for i in coutn1.keys() is same as for i in count1:

''' 

a = dict()

print(dir(a))