import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

x = [5,4,7,6,8,9,2,4,7,4,7,11]
y = [92,96,84,76,99,102,89,107,89,84,72,93]

slope, intercept, r, p, sttd-error = stats.linregress(x, y)

def model(x):
    return slope * x + intercept

model_regression = list(map(model, x))

plt.scatter(x,y)
plt.plot(x, model_regression)
