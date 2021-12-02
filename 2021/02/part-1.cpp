#include <string>
#include <iostream>

int main() {
	int horizontal_position = 0;
	int depth = 0;
	std::string direction;
	unsigned int distance;
	while (std::cin >> direction >> distance) {
		if (direction == "forward")
			horizontal_position += distance;
		else if (direction == "down")
			depth += distance;
		else if (direction == "up")
			depth -= distance;
	}
	std::cout << horizontal_position << " * " << depth << " = " << horizontal_position * depth << std::endl;
	return 0;
}
