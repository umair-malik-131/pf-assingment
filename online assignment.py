#M01 removing 2'S
"""a = [1, 2, 4, 2, 5, 2, 6]
b = []
for x in a:
    if x != 2:
        b.append(x)
print(b)"""  

# M02 SECOND LARGEST
"""n = [9, 2, 11, 7, 11, 3]
largest = None
second = None
for x in n:
    if x not in [largest, second]:
        if largest is None or x > largest:
            second = largest
            largest = x
        elif second is None or x > second:
            second = x
print(second)"""

# M03 ROTATE LEFT BY ONE
"""a = [10, 20, 30, 40, 50]
first = a[0]
for i in range(len(a) - 1):
    a[i] = a[i + 1]
a[-1] = first
print(a)""" 

# M04 INSERT VALUE 99 AT INDUX K
"""a = [1, 2, 3, 4, 5]
k = 2
a.append(0)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = 99
print(a)"""  

# M05 DELETING THE ELEMENT
"""a = [5, 6, 7, 8, 9, 10]
k = 2
for i in range(k, len(a) - 1):
    a[i] = a[i + 1]
a.pop()
print(a)"""  

# M06 PRINT THE LONGEST WORD AND LEN
"""line = "the quick brown fox"
words = line.split()
longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w
print("words=", longest,"length is =", len(longest))"""

#M07 split into words, then join using " | " as separator and print
"""s = "hello world foo bar"
words = s.split()
n = " | ".join(words)
print(n)"""

#M08 create a new list of unique elements preserving order
"""a = [3, 3, 2, 3, 1, 2, 4, 4]
u = []
for x in a:
    if x not in u:
        u.append(x)
print(u)""" 

#M09 create a new list of unique elements preserving order.
"""a = [1, 1, 1, 2, 2, 3, 4, 4]
seen = []
for x in a:
    if x in seen:
        continue
    count = 0
    for y in a:
        if y == x:
            count += 1
    print(x, "->", count)
    seen.append(x)"""

#M10 sort in ascending order using bubble sort
"""a = [8, 3, 5, 2, 9, 1]
n = len(a)
for p in range(n - 1):
    for i in range(n - 1 - p):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
print(a)"""