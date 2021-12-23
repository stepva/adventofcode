import hashlib

# INPUT
key = ""

i = 1
hexhash = hashlib.md5(key.encode()).hexdigest()

while hexhash[:5] != "00000":
    test = key + str(i)
    hexhash = hashlib.md5(test.encode()).hexdigest()
    i += 1

# ANSWER 1
print(i - 1)

i = 1
hexhash = hashlib.md5(key.encode()).hexdigest()

while hexhash[:6] != "000000":
    test = key + str(i)
    hexhash = hashlib.md5(test.encode()).hexdigest()
    i += 1

# ANSWER 2
print(i - 1)
