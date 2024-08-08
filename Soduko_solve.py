def display_sudoku(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def is_move_valid(grid, row_idx, col_idx, number):
    for i in range(9):
        if grid[row_idx][i] == number or grid[i][col_idx] == number:
            return False

    start_row, start_col = 3 * (row_idx // 3), 3 * (col_idx // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == number:
                return False

    return True

def solve_grid(grid):
    for row_idx in range(9):
        for col_idx in range(9):
            if grid[row_idx][col_idx] == 0:
                for number in range(1, 10):
                    if is_move_valid(grid, row_idx, col_idx, number):
                        grid[row_idx][col_idx] = number
                        if solve_grid(grid):
                            return True
                        grid[row_idx][col_idx] = 0
                return False
    return True

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_grid(puzzle):
    print("Solved Sudoku:")
    display_sudoku(puzzle)
else:
    print("No solution exists for Sudoku.")
