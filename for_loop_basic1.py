for i in range(0, 151):
    print(i)

for j in range(5, 1005, 5):
    print(j)

for c in range(1, 101):
    if c % 10 == 0:
        print("Coding Dojo")
    elif c % 5 == 0:
        print("Coding")
    else:
        print(c)

total_sum = 0
for t in range(1, 500001, 2):
    total_sum += t
print(total_sum)

for d in range(2018, 0, -4):
    print(d)

lowNum = 2
highNum = 9
mult = 3

for l in range(lowNum, highNum + 1):
    if l % mult == 0:
        print(l)
