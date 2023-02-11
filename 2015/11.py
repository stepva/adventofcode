import re

old = "vzbxkghb"

rgx = re.compile(r"(.)\1")


def check(psw):
    if any([ord(c) in psw for c in ["i", "o", "l"]]):
        return False

    psw_word = "".join([chr(x) for x in psw])
    res = rgx.findall(psw_word)
    if len(set(res)) < 2:
        return False

    straight = False
    for i in range(5):
        if psw[i] - psw[i + 1] == -1 and psw[i + 1] - psw[i + 2] == -1:
            straight = True
            break
    if not straight:
        return False

    return True


old_ord = [ord(c) for c in old]

while not check(old_ord):
    for i in range(8):
        if old_ord[i] > ord("z"):
            old_ord[i] = ord("a")

    old_ord[7] += 1

    i = 7
    while True:
        if old_ord[i] == ord("z"):
            old_ord[i - 1] += 1
            i -= 1
        else:
            break


new = "".join([chr(x) for x in old_ord])
# ANSWER 1
print(new)

old_ord = [ord(c) for c in new]
old_ord[7] += 1

while not check(old_ord):
    for i in range(8):
        if old_ord[i] > ord("z"):
            old_ord[i] = ord("a")

    old_ord[7] += 1

    i = 7
    while True:
        if old_ord[i] == ord("z"):
            old_ord[i - 1] += 1
            i -= 1
        else:
            break


new = "".join([chr(x) for x in old_ord])
# ANSWER 2
print(new)

# at first I had a mistake there which took me a while to figure out:
# I immediatelly went from "z" to "a", without checking a password with "z" in it

# also on reddit later I found some cool reasoning and ways to do this very simply just in your head,
# realizing some simple rules and ways for how the final password has to look like
