real_input = ["Time:        40     81     77     72","Distance:   219   1012   1365   1089"]
sample = ["Time:      7  15   30","Distance:  9  40  200"]
# ===

speed = lambda s: s
distance = lambda v, t: v*t


times, dists = real_input[0], real_input[1]
times = [t for t in times.split(":")[1].strip().split(" ") if t != ""]
dists = [d for d in dists.split(":")[1].strip().split(" ") if d != ""]

time = int("".join(times))
dist = int("".join(dists))

moes = 1

# for time, dist in zip(times, dists):
duration = []
min_speed = dist//time

for i in range(time):
    v = speed(i)
    d = distance(v, time-i)
    if d > dist:
        duration.append(i)
        # if v >= min_speed: speeds.append(i)
        # print(f"Expected distance {d} beats record {dist}")
        
moes *= len(duration)
# print(duration)

# moe = 1
# for n in duration: moe *= n
# print(f"Margin of error: {duration}")
            
    
print(moes)