a = 12
b = 11
#c = a + b
#print("Sum is",c)
print("Sum is",c := a + b)
print("Sum of", a, "and", b, "is", c)

print("Sum is %d"%c)
print("Sum of %d and %d is %d"%(a,b,c))

print("Sum is {}".format(c))
print("Sum of {} and {} is {}".format(a,b,c))
print("Sum of {1} and {0} is {2}".format(a,b,c))

# f-string
print(f"Sum of {a} and {b} is {c}")
print(f"Sum of {a=} and {b=} is {c=}")

# Multi-line Print
d = a - b
e = a * b
f = a / b
print(f"""
1. Add is {c}
2. Sub is {d}
3. Mul is {e}
4. Div is {f}
""")
