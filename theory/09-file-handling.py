# file handling

# writing to a file
with open("notes.txt", "w") as f:
    f.write("Python is fun\n")
    f.write("Learning file handling\n")

# reading the whole file
with open("notes.txt", "r") as f:
    print(f.read())

# reading line by line
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())

# adding to the end of a file
with open("notes.txt", "a") as f:
    f.write("One more line\n")

with open("notes.txt", "r") as f:
    print(f.read())


# Sample output:
# Python is fun
# Learning file handling
# 
# Python is fun
# Learning file handling
# Python is fun
# Learning file handling
# One more line
