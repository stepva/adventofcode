# %%
import numpy as np

a = np.loadtxt("2021/input_1.txt")

# %%
# ANSWER 1
print(sum(a[i] > a[i - 1] for i in range(1, len(a))))

# %%
# ANSWER 2
print(sum(sum(a[i : i + 3]) > sum(a[i - 1 : i + 2]) for i in range(1, len(a - 3))))
