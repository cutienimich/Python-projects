f1 = 0
f2 = 1

print(f1)
print(f2)

for i in range(2, 10):  
    newN = f1 + f2
    print(newN)
    f1 = f2
    f2 = newN
