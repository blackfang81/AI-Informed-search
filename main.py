def is_valid(board, row, col, num):
    return (
        all(num != board[row][j] for j in range(9)) and
        all(num != board[i][col] for i in range(9)) and
        all(num != board[i][j] for i in range(row//3*3, (row//3+1)*3) for j in range(col//3*3, (col//3+1)*3))
    )

def empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def heuristic(board):
    return sum(row.count(0) for row in board)

def ida_star(board, g, threshold):
    h = heuristic(board)
    f = g + h
    if f > threshold:
        return f
    if h == 0:
        return True
    min_cost = float('inf')
    row, col = empty_cell(board)
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            cost = ida_star(board, g + 1, threshold)
            if cost is True:
                return True

            min_cost = min(min_cost, cost)
            board[row][col] = 0
    return min_cost

def solve(board):
    threshold = heuristic(board)
    while True:
        result = ida_star(board, 0, threshold)
        if result is True:
            return board

        if result == float('inf'):
            return None
        threshold = result

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        sudoku_board = [[int(cell) for cell in line.split()] for line in lines]
    return sudoku_board

def write_file(file_path, result):
    with open(file_path, 'w') as file:
        for row in result:
            file.write(' '.join(map(str, row)) + '\n')


if __name__ == "__main__":
    input_board = read_file('input.txt')
    result = solve(input_board)
    write_file('output.txt', result)
