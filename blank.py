import math
import numpy as np

n = 0
t = 2500000
r = 100000
while t <5000000:
    t = t + (r*0.9+((r*0.9)/(5*55)))
    print(t)

    n+=1
print(n)
