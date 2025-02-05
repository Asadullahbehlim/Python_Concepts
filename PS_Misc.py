# Python to program to see highest no.

def func(val1,val2,val3):
    print("Highest value is : ",max(val1,val2,val3))
func(23,45,21)

# Create a func to create print a list, where values are square of nos b/w 1 & 30.

def a_list():
    list = []
    for i in range(1,31):
        list.append(i*i)
    return list
print(a_list())

# Alternate approach
def my_list():
    return [i*i for i in range(1,41)]
print(my_list())

# check prime no
def check_prime(num):
    if num == 1:
        print("Its not a prime no")
    if num == 2:
        print("Its a prime no.")
        return

    for i in range(2,num):
            if num % i == 0:
                print("Its not a prime no.")
                break
    else:
        print("Its a prime no")

check_prime(2)

#add in list
def add(a,b):
    print(a+b)
add(32,34)

def add_any(*nums):  # Arbitrary argument - Jitna lena hai lo
    return sum(nums)
res1 = add_any(12,34,56,1,544,23)
print(res1)
res2 = add_any(11,2,3,4,4,5,)
print(res2)

#fibonacci series by recursion (number at place)
def fs(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    else:
        return (fs(num-1) + fs(num-2))
print(fs(20))

