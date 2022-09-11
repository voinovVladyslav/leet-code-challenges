def gameOfLife(board: list[list[int]]) -> None:
    n = len(board)
    m = len(board[0])
    t = []
    for i in board:
        t.append(i.copy())
    for i in range(n):
        for j in range(m):
            sum = 0
            if i - 1 >= 0:
                sum += board[i - 1][j]            # up

            if j + 1 < m:
                sum += board[i][j + 1]            # right

            if j - 1 >= 0:
                sum += board[i][j - 1]            # left
                

            if j - 1 >= 0 and i - 1 >= 0:         # up left
                sum += board[i - 1][j - 1]

            if j + 1 < m and i - 1 >= 0:
                sum += board[i - 1][j + 1]        # up right

            if i + 1 < n:
                sum += board[i + 1][j]            # down
                if j + 1 < m:
                    sum += board[i + 1][j + 1]    # down rigth
                if j - 1 >= 0:
                    sum += board[i + 1][j - 1]    # down left
            
            t[i][j] = sum

    for i in range(n):
        for j in range(m):
            if t[i][j] < 2:
                board[i][j] = 0
            if t[i][j] > 3:
                board[i][j] = 0
            if t[i][j] == 3:
                board[i][j] = 1

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

gameOfLife(board)

for i in board:
    print(i)