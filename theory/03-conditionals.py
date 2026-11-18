# if elif else

marks = 78

if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("A-")
elif marks >= 50:
    print("B")
else:
    print("Need to study more")

# nested if
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("you can enter")
    else:
        print("bring your id")
else:
    print("too young")

# short way - ternary operator
num = 7
result = "even" if num % 2 == 0 else "odd"
print(result)


# Sample output:
# A
# you can enter
# odd
