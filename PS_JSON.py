# Convert following dictionary into JSON format
import json

student_data = { "name": "David", "age":13, "marks":85 }
data = json.dumps(student_data)
print(data)
print(type(student_data))

# Access the value of name given from the JSON data.

student_data = { "name": "David", "age":13, "marks":85 }
name = student_data["name"]
print(name)

# Q) Write a python program to sort a dictionary by value.

a = {"a":23,"b":33,"c":12,"d":27,"e":39}
a = sorted(a.values())
print(a)

# Q) 1 to 15 nos and square

d = {}

for i in range(1,16):
     d[i] = i*i
print(d)

# Q) Multiply all no in dictionary

c =  {"a":23,"b":33,"c":12,"d":27,"e":39}
j = 1
for i in c:
     j = c[i] * j
print(j)

