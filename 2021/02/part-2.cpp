#include <string>
#include <iostream>

int main() {
	int horizontal_position = 0;
	int aim = 0;
	int depth = 0;
	std::string direction;
	unsigned int distance;
	while (std::cin >> direction >> distance) {
		if (direction == "forward") {
			horizontal_position += distance;
			depth += distance * aim;
		} else if (direction == "down")
			aim += distance;
		else if (direction == "up")
			aim -= distance;
	}
	std::cout << horizontal_position << " * " << depth << " = " << horizontal_position * depth << std::endl;
	return 0;
}
