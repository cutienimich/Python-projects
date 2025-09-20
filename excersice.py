i = 0
j = 1

print(i)
print(j)


for x in range(10):
    newNum = i + j
    i= j
    j = newNum
    print(newNum + i)