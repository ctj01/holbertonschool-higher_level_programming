#!/usr/bin/python3
import sys

"""
N Queens main file. For creating a program that solves the nqueens algorithm.
"""


class Chess:
    """ Chess class. For creating a 2d array chessboard dealie. """
    def __init__(self, n, queens=0):
        """
        takes 'n', the size of the board, and optionally,
        queens, number of queens already solved
        """
        self.board = list()
        self.queens = queens
        for x in range(n):
            self.board += [['0' for x in range(n)]]

    def __repr__(self):
        """
        prints board all prettylike
        """
        string = ""
        for n in range(len(self.board)):
            string += str(self.board[n]) + '\n'
        return (string)


def place_queen(board, row, col):
    """
    places a queen onto a board and apply 'ripple'
    """
    board.board[row][col] = 'Q'
    board = ripple(board, (row, col))
    return (board)


def copy_board(board):
    """
    copies a board (not allowed to use deep copy)
    """
    newBoard = Chess(len(board.board), board.queens)
    for c in range(len(board.board)):
        for x in range(len(board.board)):
            newBoard.board[c][x] = board.board[c][x]
    return (newBoard)


def ripple(board, pos):
    """
    ripple: applies an 'x' on every square the queen would be able to attack
    """
    for count in range(len(board.board)):
        for n in range(len(board.board)):
            if count == pos[0] and n == pos[1]:
                pass
            elif (count == pos[0] or n == pos[1] or
                  (pos[0] + pos[1]) == (count + n) or
                  (pos[0] - pos[1]) == (count - n)):
                board.board[count][n] = 'x'
    return (board)

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)


try:
    n = int(sys.argv[1])
except:
    print("N must be a number")
    exit(1)
if n < 4:
    print("N must be at least 4")
    exit(1)


def main():
    board = Chess(int(sys.argv[1]))
    possible = []

    row = 0

    for col in range(n):
        if board.board[row][col] == '0':
            newBoard = copy_board(board)
            place_queen(newBoard, row, col)
            newBoard.queens += 1
            possible += [newBoard]

    solutions = []

    for board in possible:
        row = 1
        for row in range(1, n):
            col = 0
            for col in range(0, n):
                if board.board[row][col] == '0':
                    newBoard = copy_board(board)
                    place_queen(newBoard, row, col)
                    newBoard.board[row][col] = 'Q'
                    newBoard.queens += 1
                    if newBoard.queens == n:
                        solutions += [newBoard]
                    elif newBoard.queens == row:
                        if (row < (n - 1) and
                                newBoard.board[row + 1].count('0') == 0):
                            pass
                        else:
                            possible += [newBoard]

    ret = []
    for board in solutions:
        solution = []
        for row in range(n):
            for col in range(n):
                if board.board[row][col] == 'Q':
                    solution += [[row, col]]
                    if solution not in ret:
                        ret += [solution]

    for x in ret:
        print(x)

if __name__ == "__main__":
    main()

"""
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
"""
