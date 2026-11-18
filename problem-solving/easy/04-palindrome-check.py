# problem: check if a word reads the same forwards and backwards
# madam -> madam, so it is a palindrome

word = "madam"

if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")


# Sample output:
# madam is a palindrome
