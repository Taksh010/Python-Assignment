'''
Name: Taksh Patel
Roll no: 24BEE208
Branch: Electrical Engineering
'''

# 1. Three functions in a list
def fun():
    print("fun called")
def disp():
    print("disp called")
def msg():
    print("msg called")

lst = [fun, disp, msg]
for f in lst:
    f()

# 2. Map + lambda with two lists
l1 = [1, 2, 3, 4, 5, 6]
l2 = [6, 5, 4, 3, 2, 1]
res = list(map(lambda x, y: x + y, l1, l2))
print(res)

# 3. 10 random numbers between -15 and 15, get their squares
import random
nums = random.sample(range(-15, 16), 10)
squares = list(map(lambda x: x**2, nums))
print(nums)
print(squares)

# 4. Print palindromes only
lst = ['madam', 'Python', 'malayalam', 12321]
for item in lst:
    s = str(item)
    if s == s[::-1]:
        print(s)

# 5. Filter names with length > 8
names = ["Taksh", "Patel", "Ravindra", "Aishwarya", "Christopher", "Neel", "Pranav", "Mohammed"]
long_names = [name for name in names if len(name) > 8]
print(long_names)

