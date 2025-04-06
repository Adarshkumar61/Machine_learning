# example of simple linear_modell:
import matplotlib.pyplot as plt
from sklearn import linear_model
import pandas as pd
import numpy as np
from scipy import stats

x = [3.5, 3.69, 3.44, 3.43, 4.34, 4.22, 2.37]
y = [18, 15, 18, 16, 15, 14, 24]

slope , r, p, intercept, stt_err = stats.linregress(x, y)
