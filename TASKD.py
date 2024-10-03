import math
data = list(input().split())
result = 0
for i in range(len(data)):
    result += int(data[i]) ** 2
result = math.sqrt((result)/len(data))
print(round(result,3))