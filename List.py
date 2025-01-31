# Lists - We can collection of ordered & mutable data in lists.
# Multiple data type can be stored in a single list.

players = ["Virat","Abd","kallis","Ponting"]
print(players)
print(type(players))
print(players[::]) # slicing

# List Iteration
# Iteration Using for loop
players = ["Virat","Abd","kallis","Ponting"]
for i in range(len(players)):
    print(players[i])

# marvel whle loop
a = ["Hulk", "Thor", "Iron man","Capt America"]
i=0
while i<(len(a)):
        print(a[i])
        i = i +1

players = ["Virat","Abd","kallis","Ponting"]
# To add to the list
players.append("Maxwell")
print(players)

# add to a specific location/index
players.insert(1,"warner")
print(players)

# To remove from a list
players.remove("warner")
print(players)

# To remove from certain location
print(players.pop(2))
print(players)

# Copy list
players2 = players.copy()
print(players2)

# to access an element
print(players.index("Abd"))

# To extend a list

players3 = ["starc", "Bumrah"]
players.extend(players3)
print(players)
# To reverse a list
print(players[::-1])   # Method 1
players.reverse()      # Method 2
print(players)

# To sort a list
players.sort()
print(players)

# clear all data
players.clear()
print(players)

# List comprehension

l1 = [30,30,50,60]
l2= []

for i in l1:
    if i>32:
      l2.append(i)

print(l1,"\n",l2)

# List comprehension Part 2 ===
l3 = [i for i in l1>43 ]
print(l3)
