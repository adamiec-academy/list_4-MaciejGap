def info(data):
    for row in data:
        for element in row:
            print(element, end="")
        print()


def border_map(a, b):
    board = []
    for i in range(b):
        board.append(a * ["."])
    for i in range(a):
        board[0][i] = "X"
        board[b - 1][i] = "X"
    for i in range(b):
        board[i][0] = "X"
        board[i][a - 1] = "X"
    return board

