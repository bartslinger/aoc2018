#!/usr/bin/env python3

def winning_score(players, last_worth):
	points = [0] * players
	circle = [0]
	value = 0
	current = 0
	player = -1
	for value in range(1, last_worth+1):
		player += 1
		player = player % players
		if value % 23 == 0:
			# keep marble
			points[player] += value
			points[player] += circle[current-7]
			current = (current - 7) % len(circle)
			del circle[current]
			# wat if last one was deleted
			if current == len(circle):
				print("tja")
		else:
			place_idx = (current+2)
			if place_idx == len(circle)+1:
				place_idx = 1
			circle.insert(place_idx, value)
			current = place_idx

	return(max(points))

# tests
assert winning_score(9, 25) == 32
assert winning_score(10, 1618) == 8317
assert winning_score(13, 7999) == 146373
assert winning_score(17, 1104) == 2764
assert winning_score(21, 6111) == 54718
assert winning_score(30, 5807) == 37305

# Using puzzle input:
print("Answer 1:", winning_score(418, 71339))
print("Answer 2:", winning_score(418, 71339*100))
