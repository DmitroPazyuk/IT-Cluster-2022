board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

# 2 player => "0" and "x"

active_player = "0"


def is_win(board, player):
    # check rows for win combination
    for row_i in range(len(board)):
        win = True
        for col_i in range(len(board)):
            if board[row_i][col_i] != player:
                win = False
        if win:
            return True

    # check cols for win combination
    for col_i in range(len(board)):
        win = True
        for row_i in range(len(board)):
            if board[row_i][col_i] != player:
                win = False
        if win:
            return True

    # check diagonal for win combination
    win = True
    for i in range(len(board)):
        if board[i][i] != player:
            win = False
    if win:
        return True

    # todo check diagonal 2 for win combination
    return False


def change_player(active_player):
    if "0" == active_player:
        return "x"
    else:
        return "0"


while True:
    try:
        print(f"Player {active_player} move")
        for row in board:
            for i in row:
                print(f"{i} ", end="")
            print()

        data = input("Enter row and column numbers to fix spot: ").split(" ")
        if len(data) != 2:
            raise KeyError("Error! Input data have to be:1 2")
        row, col = int(data[0]) - 1, int(data[1]) - 1
        print(data)

        if board[row][col] == "-":
            board[row][col] = active_player
        else:
            print("the spot is taken. Choose another")
            continue

        if is_win(board, active_player):
            print(f"Player {active_player} win!!!")
            break

        active_player = change_player(active_player)
    except KeyError as e:
        print(e)

    except IndexError:
        print("Indexes must be in range 1-3")

    except Exception:
        print("Ups!!!")