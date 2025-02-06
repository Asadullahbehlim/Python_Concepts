a = "cricket","football","hockey",1.45,2    # Tuple with or without bracket
print(type(a)) # Tuple is unmutable cant add delete append etc won't work

# for loop
for i in a:
    print(i)

# along with range
for i in range(len(a)):
    print(i)

# Tuple conversion and all

b = "fintech","biztalk", "uitalk"
print("before conversion", type(b))
b = list(b)
b.append("sharktank")
print("after conversion", type(b))
b = tuple(b)
print(b)
print("final conversion", type(b))
print((b.index("uitalk")))

#Dictionary - access

employee_data = {"name":"Asad", "Age": 26 }
print(employee_data["name"])


# only keys needed
employee_data = {"name":"Asad", "Age": 26 }

for i in employee_data:
    print(i)

# When value needed

employee_data = {"name":"Asad", "Age": 26 }

for i in employee_data:
    print(employee_data[i])


# when both needed using items function

employee_data = {"name":"Asad", "Age": 26 }

for i,j in employee_data.items():
    print(i,"-", j)

# Get item, keys, value, copy

i = employee_data.get("name")
print(i)

a = employee_data.items()
print(a)

# Keys/values
b = employee_data.keys()
print(b)

# copy
d = employee_data.copy()
print(d)

# Iteration in dictionaries

Career_stats = {"name":"kohli","century":"81"}
z = Career_stats.setdefault("avg", 55)
print(Career_stats)
print(z)

# Nested Dictionary

Employee = { 1: { "name": "abd", "age":"38"},
             2: {"name":"kallis", "age": "43" }}
print(Employee[2]["name"])



