# problem: count how many times each word appears in a sentence

text = "python is fun and python is easy to learn"
words = text.split()

freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print(freq)

# most common word
most = max(freq, key=freq.get)
print("most common:", most, "-", freq[most], "times")


# Sample output:
# {'python': 2, 'is': 2, 'fun': 1, 'and': 1, 'easy': 1, 'to': 1, 'learn': 1}
# most common: python - 2 times
