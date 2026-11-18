# tuples - cannot be changed after creation

point = (3, 4)
print(point[0], point[1])

# unpacking
x, y = point
print(x, y)

# dictionaries - key value pairs
student = {
    "name": "Shahnewaj",
    "dept": "Physics",
    "cgpa": 3.52
}

print(student["name"])
print(student.get("age", "not given"))  # get with default value

student["cgpa"] = 3.60
student["year"] = "final"
print(student)

for key, value in student.items():
    print(key, ":", value)

# sets - no duplicates, no order
nums = {1, 2, 2, 3, 3, 3}
print(nums)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)  # union
print(a & b)  # intersection
print(a - b)  # difference


# Sample output:
# 3 4
# 3 4
# Shahnewaj
# not given
# {'name': 'Shahnewaj', 'dept': 'Physics', 'cgpa': 3.6, 'year': 'final'}
# name : Shahnewaj
# dept : Physics
# cgpa : 3.6
# year : final
# {1, 2, 3}
# {1, 2, 3, 4, 5, 6}
# {3, 4}
# {1, 2}
