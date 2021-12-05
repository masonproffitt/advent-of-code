#include <stdio.h>

#define MAX_N_DRAWN_NUMBERS 256
#define MAX_N_BOARDS 256
#define N_ROWS 5
#define N_COLUMNS 5

unsigned get_drawn_numbers(FILE *const stream, unsigned *const array)
{
	unsigned n_drawn_numbers = 0;
	char c = 0;
	do {
		if (n_drawn_numbers > MAX_N_DRAWN_NUMBERS)
			break;
		int match = fscanf(stream, "%u", array + n_drawn_numbers);
		if (match > 0)
			++n_drawn_numbers;
		c = fgetc(stream);
	} while (c != '\n');
	return n_drawn_numbers;
}

void print_drawn_numbers(const unsigned *const drawn_numbers, const unsigned n_drawn_numbers)
{
	printf("Drawn numbers (%u):", n_drawn_numbers);
	for (int i = 0; i < n_drawn_numbers; ++i)
		printf(" %u,", drawn_numbers[i]);
}

unsigned get_boards(FILE *const stream, unsigned (*const array)[N_ROWS][N_COLUMNS])
{
	unsigned n_boards = 0;
	unsigned row_index = 0;
	unsigned column_index = 0;
	char c = 0;
	do {
		if (n_boards > MAX_N_BOARDS)
			break;
		int match = fscanf(stream, "%u", array[n_boards][column_index] + row_index);
		if (match > 0)
			++column_index;
		if (column_index >= N_COLUMNS) {
			++row_index;
			column_index = 0;
		}
		if (row_index >= N_ROWS) {
			++n_boards;
			row_index = 0;
		}
		c = fgetc(stream);
	} while (c != EOF);
	return n_boards;
}

void print_boards(const unsigned (*const boards)[N_ROWS][N_COLUMNS], const unsigned n_boards)
{
	printf("Boards (%u):\n", n_boards);
	for (int board_index = 0; board_index < n_boards; ++board_index) {
		for (int row_index = 0; row_index < N_ROWS; ++row_index) {
			for (int column_index = 0; column_index < N_COLUMNS; ++column_index)
				printf("%2u ", boards[board_index][row_index][column_index]);
			printf("\n");
		}
		printf("\n");
	}
}

void initialize_marked_spaces(const unsigned n_boards, int (*const marked_spaces)[N_ROWS][N_COLUMNS])
{
	for (int board_index = 0; board_index < n_boards; ++board_index) {
		for (int row_index = 0; row_index < N_ROWS; ++row_index) {
			for (int column_index = 0; column_index < N_COLUMNS; ++column_index)
				marked_spaces[board_index][row_index][column_index] = 0;
		}
	}
}

void mark_boards(const unsigned (*const boards)[N_ROWS][N_COLUMNS], const unsigned n_boards, const unsigned drawn_number, int (*const marked_spaces)[N_ROWS][N_COLUMNS])
{
	for (int board_index = 0; board_index < n_boards; ++board_index) {
		for (int row_index = 0; row_index < N_ROWS; ++row_index) {
			for (int column_index = 0; column_index < N_COLUMNS; ++column_index) {
				if (boards[board_index][row_index][column_index] == drawn_number)
					marked_spaces[board_index][row_index][column_index] = 1;
			}
		}
	}
}

int did_board_win(const int marked_spaces[N_ROWS][N_COLUMNS])
{
	for (int row_index = 0; row_index < N_ROWS; ++row_index) {
		int row_flag = 1;
		for (int column_index = 0; column_index < N_COLUMNS; ++column_index) {
			if (! marked_spaces[row_index][column_index]) {
				row_flag = 0;
				break;
			}
		}
		if (row_flag)
			return 1;
	}
	for (int column_index = 0; column_index < N_COLUMNS; ++column_index) {
		int column_flag = 1;
		for (int row_index = 0; row_index < N_ROWS; ++row_index) {
			if (! marked_spaces[row_index][column_index]) {
				column_flag = 0;
				break;
			}
		}
		if (column_flag)
			return 1;
	}
	return 0;
}

int find_winning_board(const unsigned n_boards, const int (*const marked_spaces)[N_ROWS][N_COLUMNS])
{
	for (int board_index = 0; board_index < n_boards; ++board_index) {
		if (did_board_win(marked_spaces[board_index]))
			return board_index;
	}
	return -1;
}

unsigned get_unmarked_sum(const unsigned board[N_ROWS][N_COLUMNS], const int marked_spaces[N_ROWS][N_COLUMNS])
{
	unsigned sum = 0;
	for (int row_index = 0; row_index < N_ROWS; ++row_index) {
		for (int column_index = 0; column_index < N_COLUMNS; ++column_index) {
			if (! marked_spaces[row_index][column_index])
				sum += board[row_index][column_index];
		}
	}
	return sum;
}

int main()
{
	unsigned drawn_numbers[MAX_N_DRAWN_NUMBERS] = {};
	const unsigned n_drawn_numbers = get_drawn_numbers(stdin, drawn_numbers);
	print_drawn_numbers(drawn_numbers, n_drawn_numbers);

	unsigned boards[MAX_N_BOARDS][N_ROWS][N_COLUMNS] = {};
	const unsigned n_boards = get_boards(stdin, boards);
	print_boards(boards, n_boards);

	int marked_spaces[n_boards][N_ROWS][N_COLUMNS];
	initialize_marked_spaces(n_boards, marked_spaces);
	unsigned winning_boards[n_boards];
	unsigned n_winning_boards = 0;
	for (int board_index = 0; board_index < n_boards; ++board_index)
		winning_boards[board_index] = 0;
	for (int drawn_number_index = 0; drawn_number_index < n_drawn_numbers; ++drawn_number_index) {
		const unsigned drawn_number = drawn_numbers[drawn_number_index];
		mark_boards(boards, n_boards, drawn_number, marked_spaces);
		for (int board_index = 0; board_index < n_boards; ++board_index) {
			if (winning_boards[board_index] == 0) {
				if (did_board_win(marked_spaces[board_index])) {
					winning_boards[board_index] = 1;
					++n_winning_boards;
					const unsigned unmarked_sum = get_unmarked_sum(boards[board_index], marked_spaces[board_index]);
					const unsigned score = unmarked_sum * drawn_number;
					printf("Winning board %u / %u (index %u) score: %u * %u = %u\n", n_winning_boards, n_boards, board_index, unmarked_sum, drawn_number, score);
				}
			}
		}
	}
	return 0;
}
