# %%
import pandas as pd

df = pd.read_csv("2021/input_3.txt", header=None, dtype=str)

# %%
df1 = df[0].apply(lambda x: pd.Series(list(x)))
gam = df1.apply(lambda x: x.mode(), axis=0)

# %%
gam = gam.apply(lambda x: "".join(x), axis=1)[0]
eps = "".join(["0" if c == "1" else "1" for c in gam])

# %%
def from_bin(s):
    n = 0
    s = s[::-1]
    for i in range(0, len(s)):
        n += int(s[i]) * pow(2, i)

    return n


# ANSWER 1
print(from_bin(gam) * from_bin(eps))

# %%
df2 = df[0].apply(lambda x: pd.Series(list(x)))
ncols = len(df2.columns)

# %%
df2_oxy = df2.copy()
for i in range(0, ncols):
    if df2_oxy.shape[0] > 1:
        test = df2_oxy[df2_oxy[i] == df2_oxy[i].mode()[0]]
        if test.shape[0] * 2 == df2_oxy.shape[0]:
            df2_oxy = df2_oxy[df2_oxy[i] == "1"].reset_index(drop=True)
        else:
            df2_oxy = test.reset_index(drop=True)

oxy = df2_oxy.apply(lambda x: "".join(x), axis=1)[0]

# %%
df2_co2 = df2.copy()
for i in range(0, ncols):
    if df2_co2.shape[0] > 1:
        test = df2_co2[df2_co2[i] != df2_co2[i].mode()[0]]
        if test.shape[0] * 2 == df2_co2.shape[0]:
            df2_co2 = df2_co2[df2_co2[i] == "0"].reset_index(drop=True)
        else:
            df2_co2 = test.reset_index(drop=True)

co2 = df2_co2.apply(lambda x: "".join(x), axis=1)[0]

# %%
# ANSWER 2
print(from_bin(oxy) * from_bin(co2))
