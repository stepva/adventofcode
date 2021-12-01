# %%
import numpy as np

a = np.loadtxt("input_1.txt")

# %%
sum(a[i] > a[i - 1] for i in range(1, len(a)))

# %%
sum(sum(a[i : i + 3]) > sum(a[i - 1 : i + 2]) for i in range(1, len(a - 3)))
