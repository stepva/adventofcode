# %%
import numpy as np

f = open('2021/input_20.txt', 'r')
lines = f.readlines()

algo = lines[0][:-1]
# %%
image = np.empty((0,len(lines[3])-1))
for l in lines[2:]:
    l = l[:-1]
    l = l.replace('.', '0')
    l = l.replace('#', '1')
    image = np.vstack([image, list(l)]).astype(int)

#%% 
def img_enhance(new, old, x, y):
    x1 = x - 1
    x2 = x1 + 3
    y1 = y - 1
    y2 = y1 + 3

    a = old[x1:x2, y1:y2]
    a = a.flatten()
    a = ''.join([str(int(x)) for x in a])
    a = int(a, 2)

    match algo[a]:
        case '.':
            new_bit = 0
        case '#':
            new_bit = 1
    
    new[x1][y1] = new_bit

# %%
for i in range(0, 2):
    x, y = image.shape
    if algo[0] == '.' or i%2 == 0:
        new_img = np.zeros((x+6, y+6))
    else:
        new_img = np.ones((x+6, y+6))
    new_img[3:x+3, 3:y+3] = image

    x, y = new_img.shape
    image = np.zeros((x-3, y-3))

    for i in range(1, x-2):
        for j in range(1, y-2):
            img_enhance(image, new_img, i, j)

# %%
# ANSWER 1
print(sum(sum(image)))

# %%
for i in range(0, 48):
    x, y = image.shape
    if algo[0] == '.' or i%2 == 0:
        new_img = np.zeros((x+6, y+6))
    else:
        new_img = np.ones((x+6, y+6))
    new_img[3:x+3, 3:y+3] = image

    x, y = new_img.shape
    image = np.zeros((x-3, y-3))

    for i in range(1, x-2):
        for j in range(1, y-2):
            img_enhance(image, new_img, i, j)

# %%
# ANSWER 2
print(sum(sum(image)))