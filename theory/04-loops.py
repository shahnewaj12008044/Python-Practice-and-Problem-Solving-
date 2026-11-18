# for loop

for i in range(5):
    print(i)

print("---")

for i in range(1, 11, 2):  # start, stop, step
    print(i)

print("---")

fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# while loop
count = 1
while count <= 5:
    print(count)
    count += 1

# break and continue
for i in range(10):
    if i == 3:
        continue  # skip 3
    if i == 7:
        break  # stop the loop
    print(i)

# nested loop - multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()


# Sample output:
# 0
# 1
# 2
# 3
# 4
# ---
# 1
# 3
# 5
# 7
# 9
# ---
# apple
# banana
# mango
# 1
# 2
# 3
# 4
# 5
# 0
# 1
# 2
# 4
# 5
# 6
# 1 2 3 
# 2 4 6 
# 3 6 9 
