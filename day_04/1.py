#!/usr/bin/env python3

import sys
import re
from datetime import datetime

# Import data
filename = 'input'
if (len(sys.argv) > 1 and sys.argv[1] == 'test'):
	filename = 'test'
	print("test mode")
f = open(filename, 'r')
lines = f.read().splitlines()
f.close()

# Order the data, just sort alphabetically
lines.sort()

guard_id = -1
guard_is_sleeping = False
fall_asleep_minute = -1

guards = {}

for line in lines:
	matchObj = re.match(r'\[(.*)\] (.*)', line)
	datetime_object = datetime.strptime(matchObj.group(1), '%Y-%m-%d %H:%M')
	if matchObj.group(2) == 'falls asleep':
		fall_asleep_minute = datetime_object.minute

	elif matchObj.group(2) == 'wakes up':
		for min in range(fall_asleep_minute, datetime_object.minute):
			guards[guard_id][min] += 1

	else:
		# Match guard ID
		if guard_is_sleeping:
			print("guard was sleeping while other started")
			exit(-1)
		guard_id = matchObj.group(2)[7:].split(' ')[0]
		# Create record of this guard if the ID does not exist
		if guard_id not in guards:
			guards[guard_id] = [0] * 60

# Find the guard that has the most minutes asleep
max_sleep = 0
max_sleep_guard = -1
for guard_id in guards:
	guard_sleep = sum(guards[guard_id])
	if guard_sleep > max_sleep:
		max_sleep = guard_sleep
		max_sleep_guard = guard_id

slept_so_many_times = max(guards[max_sleep_guard])
slept_most_during_minute = guards[max_sleep_guard].index(slept_so_many_times)
print("Guard ID:", max_sleep_guard)
print("Asleep most in minute:", slept_most_during_minute, ",", slept_so_many_times, "times")
print("Answer 1:", slept_most_during_minute * int(max_sleep_guard))

# Now look for the guard that was most asleep during a specific minute

most_asleep_times = -1
most_asleep_in_minute = -1
most_asleep_guard_id = -1
for guard_id in guards:
	its_most_asleep_times = max(guards[guard_id])
	if its_most_asleep_times > most_asleep_times:
		most_asleep_times = its_most_asleep_times
		most_asleep_in_minute = guards[guard_id].index(its_most_asleep_times)
		most_asleep_guard_id = guard_id

print("Part Two:")
print("Guard ID:", most_asleep_guard_id)
print("Times asleep in a single minute:", most_asleep_times)
print("In minute:", most_asleep_in_minute)
print("Answer 2:", int(most_asleep_guard_id) * most_asleep_in_minute)
