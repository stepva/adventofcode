import numpy as np
from numpy.lib.function_base import median

c = np.loadtxt("2021/input_7.txt", delimiter=",")

# ANSWER 1
print(sum(abs(c - median(c))))

# ANSWER 2
print(sum((abs(c - int(np.mean(c)))) * (abs(c - int(np.mean(c))) + 1) / 2))
