"""Parallel Lists"""


# Parallel iteration
"""odds = []"""
lst_a = [1, 32, 15, 7, 3, 9, 16, 13, 22, 8]
lst_b = [51, 6, 25, 2, 18, 19, 21, 14, 4, 11]

"""for num in lst_a:
    if num % 2 == 1:
        odds.append(num)

for num in lst_b:
    if num % 2 == 1:
        odds.append(num)

print(odds, "\n")


# Alternative using a 'zip' object
odds = []
for a, b in zip(lst_a, lst_b):
    if a % 2 == 1:
        odds.append(a)
    if b % 2 == 1:
        odds.append(b)

print(odds, "\n")


# Another example
range_a = range(10, 101, 10)
range_b = range(100, 1001, 100)
range_c = range(1000, 10001, 1000)

for a, b, c in zip(range_a, range_b, range_c):
    print(a, b, c)
print("\n") """

"""
# Parallel iteration with 'enumerate'
def polynomial(coefs, x):
    res = 0
    n = len(coefs) - 1 # The degree of the polynomial

    for idx, val in enumerate(coefs):
        res += val * x**(n - idx)

    return res

# 2x^3 + 3x^2 + x + 6 evaluated at x = 12
print(polynomial([2, 3, 1, 6], 12), "\n") """
"""

# Enumerate and zip tuples
for tup in enumerate([9, 0, 2, 1, 0]):
    print(tup)
print("\n")


for tup in zip("abc", [1, 2, 3]):
    print(tup)
print("\n")

"""
# Using enumerate and zip together
lst_a = [1, 3, 5, 7]
lst_b = [2, 4, 6, 8]

for tup in enumerate(zip(lst_a, lst_b)):
    print(tup)
print("\n")


enum = range(len(lst_a))
for tup in zip(enum, lst_a, lst_b):
    print(tup)
print("\n")
"""
"""
"""Galvanize Data Science Prep
https://www.galvanize.com/data-science/prep"""
