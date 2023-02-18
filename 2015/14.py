import re

with open("2015/input_14.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

rgx = re.compile(r"(.+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.")

reindeers = {}

for i in instructions:
    name, speed, time, rest = rgx.search(i).groups()
    reindeers[name] = {"speed": int(speed), "time": int(time), "rest": int(rest)}

s = 2503
max_dist = 0

for r in reindeers:
    speed, time, rest = reindeers[r].values()
    total_time = time + rest
    done = (s // total_time) * time * speed
    extra = s % total_time
    extra = min(time, extra) * speed
    max_dist = max(max_dist, done + extra)

# ANSWER 1
print(max_dist)

for r in reindeers:
    reindeers[r]["distance"] = 0
    reindeers[r]["points"] = 0

current_max = 0
for si in range(1, s + 1):
    for r in reindeers:
        speed, time, rest, _, _ = reindeers[r].values()
        total_time = reindeers[r]["time"] + rest
        done = (si // total_time) * time * speed
        extra = si % total_time
        extra = min(time, extra) * speed
        reindeers[r]["distance"] = done + extra
        current_max = max(current_max, done + extra)

    for r in reindeers:
        if reindeers[r]["distance"] == current_max:
            reindeers[r]["points"] += 1

# ANSWER 2
print(reindeers[sorted(reindeers.items(), key=lambda x: x[1]["points"], reverse=True)[0][0]]["points"])

# took me a little while to get the correct calculation and formula for the distance per second
# also don't really like the 2 loops over reindeers in the second part, but first I tried just sorting them by distance every second
# and giving the point to the leader, but it doesn't work when multiple reindeers share the lead...
