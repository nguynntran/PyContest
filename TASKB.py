import math
x1, y1, x2, y2 = map(int, input().split())
matdis = abs(x2 - x1) + abs(y2 - y1)
print(matdis)