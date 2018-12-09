#include <iostream>
#include <cstdint>

struct Marble {
	uint64_t value;
	Marble* previous = nullptr;
	Marble* next = nullptr;
};

void insert_after(Marble* to_insert, Marble* after) {
	to_insert->previous = after;
	to_insert->next = after->next;
	after->next->previous = to_insert;
	after->next = to_insert;
}

void remove(Marble* remove) {
	remove->previous->next = remove->next;
	remove->next->previous = remove->previous;
	remove->previous = nullptr;
	remove->next = nullptr;
}

uint64_t play(uint64_t players, uint64_t last_marble) {
	// Make an array of all marbles
	uint64_t num_marbles = last_marble+1;
	//std::cout << "trying to allocate" << std::endl;
	Marble marbles[num_marbles];
	//std::cout << "created " << num_marbles << " marbles" << std::endl;

	// Assign values
	for (uint64_t i = 0; i < num_marbles; i++) {
		marbles[i].value = i;
		//std::cout << marbles[i].value << std::endl;
	}

	// First marble links only to itself
	marbles[0].previous = &marbles[0];
	marbles[0].next = &marbles[0];

	Marble* current_marble = &marbles[0];

	uint64_t player = 0;
	uint64_t points[players] = {0};
	// Start playing for all of the marbles
	for (uint64_t i = 1; i < num_marbles; i++) {
		//std::cout << "Player " << player << " is playing marble " << i << std::endl;
		Marble* marble_being_played = &marbles[i];
		if (marble_being_played->value % 23 == 0) {
			//std::cout << "special marble" << std::endl;
			points[player] += marble_being_played->value;
			Marble* to_remove = current_marble;
			for (uint64_t m = 0; m < 7; m++) {
				to_remove = to_remove->previous;
			}
			points[player] += to_remove->value;
			current_marble = to_remove->next;
			remove(to_remove);

		} else {
			insert_after(marble_being_played, current_marble->next);
			current_marble = marble_being_played;
		}

		if (0) {
			Marble* thisone = &marbles[0];
			do {
				std::cout << thisone->value << " ";
				thisone = thisone->next;
			} while (thisone != &marbles[0]);
			std::cout << std::endl;
		}

		// Go to next player
		player += 1;
		player %= players;
	}

	// Return most points
	uint64_t most_points = 0;
	for (uint64_t p = 0; p < players; p++) {
		if (points[p] > most_points) {
			most_points = points[p];
		}
	}
	return most_points;
}

int main() {
	Marble test_marbles[4];
	test_marbles[0].value = 10;
	test_marbles[0].next = &test_marbles[0];
	test_marbles[0].previous = &test_marbles[0];
	test_marbles[1].value = 20;
	test_marbles[2].value = 30;
	test_marbles[3].value = 40;
	insert_after(&test_marbles[1], &test_marbles[0]);
	insert_after(&test_marbles[2], &test_marbles[1]);
	insert_after(&test_marbles[3], &test_marbles[2]);
	remove(&test_marbles[1]);
	std::cout << "Some tests:" << std::endl;
	for (int i = 0; i < sizeof(test_marbles)/sizeof(Marble); i++) {
		if (test_marbles[i].previous == nullptr || test_marbles[i].next == nullptr) {
			continue;
		}
		std::cout << test_marbles[i].value << " prev: " << test_marbles[i].previous->value << " next: " << test_marbles[i].next->value << std::endl;
	}

	std::cout << "Test 1: " << play(9,25) << " == 32" << std::endl;
	std::cout << "Test 2: " << play(10,1618) << " == 8317" << std::endl;
	std::cout << "Test 3: " << play(13,7999) << " == 146373" << std::endl;
	std::cout << "Test 4: " << play(17,1104) << " == 2764" << std::endl;
	std::cout << "Test 5: " << play(21,6111) << " == 54718" << std::endl;
	std::cout << "Test 6: " << play(30,5807) << " == 37305" << std::endl;


	std::cout << "For real:" << std::endl;
	uint64_t winning_score = 0;
	winning_score = play(418, 71339);
	std::cout << "Score: " << winning_score << std::endl;
	std::cout << "Part2: " << play(418, 71339*10) << std::endl;


	return 0;
}
