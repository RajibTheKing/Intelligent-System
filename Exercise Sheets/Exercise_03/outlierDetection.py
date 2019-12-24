

import math

weights = [50, 45, 60, 70, 2, 150, 80]


mean  = 0
summation = 0
for x in weights:
    summation  = summation + x

mean = summation / len(weights)

deviation =  0

for x in weights:
    deviation = summation + ( (x - mean) * (x - mean) )

standardDeviation = math.sqrt(deviation / (len(weights) - 1))


print(mean)
print(standardDeviation)

for x in weights:
    now = abs((x - mean)) - 2 * standardDeviation
    if now > 0:
        print(str(x) + " is outlier ")











