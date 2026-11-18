# strings

name = "Shahnewaj"
print(name.upper())
print(name.lower())
print(len(name))

# slicing
print(name[0:4])
print(name[::-1])  # reverse

# f-string
age = 21
print(f"My name is {name} and I am {age} years old")

# checking things
sentence = "I love physics"
print("physics" in sentence)
print(sentence.replace("physics", "nuclear physics"))
print(sentence.split())

# joining
words = ["python", "is", "fun"]
print(" ".join(words))

# removing extra spaces
messy = "   hello   "
print(messy.strip())


# Sample output:
# SHAHNEWAJ
# shahnewaj
# 9
# Shah
# jawenhahS
# My name is Shahnewaj and I am 21 years old
# True
# I love nuclear physics
# ['I', 'love', 'physics']
# python is fun
# hello
