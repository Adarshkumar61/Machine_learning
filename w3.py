import numpy as np
from scipy import stats
#finding mean value:
# speed = [32,43, 78, 35,44, 24, 46, 35]
# x= np.mean(speed)
# print(x) #42.125

# Median:
# value = [1,23,2,3,4,5,6,78,45,3,353,53]
# xy = np.median(value)
# print(xy) #5.5 bcz there are 2 median so it added and divided by 2 : 5+6/2: 5.5

#mode:
# The Mode value is the value that appears the most number of times:

# val = [11,2,446,46,335,11, 12, 11, 3, 2, 143, 134]
# st = stats.mode(val)
# print(st) #ModeResult(mode=np.int64(11), count=np.int64(3))