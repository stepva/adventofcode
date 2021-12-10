# %%
import numpy as np

f = open("2021/input_10.txt", "r")
lines = f.readlines()

# %%
errors = []
inc_closes = []
for l in lines:
    l = l[:-1]
    need_close = []
    inc = True
    for s in l:
        match s:
            case "(":
                need_close.append(")")
            case "[":
                need_close.append("]")
            case "{":
                need_close.append("}")
            case "<":
                need_close.append(">")
            case ")":
                if need_close[-1] != s:
                    errors.append(s)
                    inc = False
                    break
                else:
                    need_close = need_close[:-1]
            case "]":
                if need_close[-1] != s:
                    errors.append(s)
                    inc = False
                    break
                else:
                    need_close = need_close[:-1]
            case "}":
                if need_close[-1] != s:
                    errors.append(s)
                    inc = False
                    break
                else:
                    need_close = need_close[:-1]
            case ">":
                if need_close[-1] != s:
                    errors.append(s)
                    inc = False
                    break
                else:
                    need_close = need_close[:-1]
    if inc:
        inc_closes.append(need_close)
# %%
values = {")": 3, "]": 57, "}": 1197, ">": 25137}
# %%
# ANSWER 1
print(np.sum(list(map(lambda x: values[x], errors))))

# %%
values2 = {")": 1, "]": 2, "}": 3, ">": 4}

#%%
scores = np.array([]) 
for i in inc_closes:
    i = list(reversed(i))
    score = 0
    for s in i:
        score = score * 5
        score += values2[s]
    scores = np.append(scores, score)

# %%
# ANSWER 2
print(np.median(scores))