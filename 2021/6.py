#%%
import numpy as np

fish = np.loadtxt("2021/input_6.txt", delimiter=",")

#%%
def get_fishes(fish, day):
    for d in range(1, day):
        fish = fish - 1
        cond = np.where(fish == -1)
        fish[cond] = 6
        fish = np.append(fish, [8] * len(cond[0]))
    return(fish)

# %%
# ANSWER 1
print(len(get_fishes(fish, 81)))

#%%
fish_128 = get_fishes(fish, 129)
unique, counts = np.unique(fish_128, return_counts=True)

#%%
fish_256 = 0
for i in range(0, len(unique)):
    fish_256 += len(get_fishes(np.array([unique[i]]), 129)) * counts[i]

#%%
# ANSWER 2
print(fish_256)