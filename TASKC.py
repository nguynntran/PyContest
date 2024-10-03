ls = []
for i in range(3):
    level, cups = input().split()
    ls.append([level, cups])
ls = ls[::-1]
sum = 0
for i in range(3):
    print(ls[i][0] + " " + ls[i][1])
    sum += int(ls[i][1]) 
print(sum)