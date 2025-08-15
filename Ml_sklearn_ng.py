import numpy as np
W = np.array([1,2,45,6,7,8,9,9])
B = np.array([0.2, 0.1, 0.1, 0.4, 0.1, 0.2,1.2, 0.3])
# f = np.dot(W, B)
W = W - 0.1 * B
print(W)