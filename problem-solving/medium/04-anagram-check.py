# problem: check if two words are anagrams of each other
# listen and silent use the same letters

word1 = "listen"
word2 = "silent"

if sorted(word1) == sorted(word2):
    print(word1, "and", word2, "are anagrams")
else:
    print("not anagrams")


# Sample output:
# listen and silent are anagrams
