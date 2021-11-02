import math

x = [0.25,0.2,0.15,0.12,0.1,0.08,0.05,0.05]
total = 0
for i in x:
    total += -1*i*math.log2(i)
y =[]
for i in x:
    y.append(-math.log2(i))
print(total)
print(y)