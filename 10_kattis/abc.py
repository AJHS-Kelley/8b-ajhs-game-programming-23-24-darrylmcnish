# input the integers
# .split() the 3 integers into separate variables
# cast the 3 variables to integers
# assign correct values from least to greatest
#A < B < C

integers = input()
a, b, c = integers.split("$")
a = int(a)
b = int(b)
c = int(c)

print(f"a: {a} b: {b} c: {c}")
if a >= b:
    a, b = b, a
if b>= c:
    b, c = c, b
print(f"a: {a} b: {b} c: {c}")   