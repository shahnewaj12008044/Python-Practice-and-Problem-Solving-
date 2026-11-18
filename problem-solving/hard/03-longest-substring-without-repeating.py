# problem: longest substring without repeating characters
# example: "abcabcbb" -> "abc", length 3

def longest_substring(s):
    seen = {}
    start = 0
    best = 0
    best_word = ""

    for i, ch in enumerate(s):
        if ch in seen and seen[ch] >= start:
            start = seen[ch] + 1
        seen[ch] = i
        if i - start + 1 > best:
            best = i - start + 1
            best_word = s[start:i + 1]

    return best_word, best

print(longest_substring("abcabcbb"))
print(longest_substring("bbbbb"))
print(longest_substring("pwwkew"))


# Sample output:
# ('abc', 3)
# ('b', 1)
# ('wke', 3)
