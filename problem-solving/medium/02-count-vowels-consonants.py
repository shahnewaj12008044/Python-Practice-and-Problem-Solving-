# problem: count vowels and consonants in a sentence

text = "Python is fun to learn"
text = text.lower()

vowels = "aeiou"
v_count = 0
c_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("vowels:", v_count)
print("consonants:", c_count)


# Sample output:
# vowels: 6
# consonants: 12
