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
