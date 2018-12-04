import numpy as np
from dateutil import parser
from collections import defaultdict
inp = [line.strip() for line in open('input')]

dates = [parser.parse(line.split(']')[0][1:]) for line in inp]
index = sorted(range(len(dates)), key=lambda k: dates[k])
inp_sorted = [inp[i] for i in index]

guard = None
guard_instr = defaultdict(list)
for instr in inp_sorted:
    instr = instr.split()
    if 'Guard' in instr[2]:
        guard = int(instr[3][1:])
        continue
    guard_instr[guard].append(instr)

guard_sleep = {g: np.array([0] * 60) for g in guard_instr.keys()}
for guard, instructions in guard_instr.items():
    sleeping = False
    for instr in instructions:
        if not sleeping:
            sleeping = True
            asleep = int(instr[1][-3:-1])
        else:
            assert 'asleep' not in instr[-1]
            sleeping = False
            wakeup = int(instr[1][-3:-1])
            sleep_tracker = guard_sleep[guard]
            sleep_tracker[asleep:wakeup] += 1
            guard_sleep[guard] = sleep_tracker

sleep_sum = [(sum(v), k) for k, v in guard_sleep.items()]
max_sleep_guard = max(sleep_sum)[1]
minute = np.argmax(guard_sleep[max_sleep_guard])
print(max_sleep_guard*minute)
max_minutes = 0
for k, v in guard_sleep.items():
    ind = np.argmax(v)
    if v[ind] > max_minutes:
        max_minutes = v[ind]
        minute = ind
        guard = k
print(guard*minute)

