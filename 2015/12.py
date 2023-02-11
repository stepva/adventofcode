import re

with open("2015/input_12.txt", "r") as f:
    instructions = f.read().replace("\n", "")

result = re.findall(r"(-*\d+)", instructions)
# ANSWER 1
print(sum([int(x) for x in result]))

import json

with open("2015/input_12.txt", "r") as f:
    json_data = json.load(f)


def search_json(j):
    result = 0

    if type(j) == int:
        return j

    if type(j) == str:
        return 0

    if type(j) == list:
        for i in j:
            result += search_json(i)
        return result

    if type(j) == dict:
        if not "red" in j.keys() and not "red" in j.values():
            for k in j.keys():
                result += search_json(k)
            for v in j.values():
                result += search_json(v)
        return result


# ANSWER 2
print(search_json(json_data))


# nice, I first solved the first part super quickly just with the regex, but second part got me
# I'm happy I was able to come up with this recursion quite quickly and all by myself
