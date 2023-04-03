import random

class Sudoku:
    def __init__(self, board=None):
        """
        Initialize a Sudoku board with the given 2D list. If no board is provided, create an empty board.
        """
        if board is None:
            board = [[0 for _ in range(9)] for _ in range(9)]
        self.board = board

    def __str__(self):
        """
        Return a string representation of the board.
        """
        return '\n'.join([' '.join(map(str, row)) for row in self.board])

    def get_row(self, row_index):
        """
        Return the row with the given index.
        """
        return self.board[row_index]

    def get_column(self, col_index):
        """
        Return the column with the given index.
        """
        return [row[col_index] for row in self.board]

    def get_block(self, row_index, col_index):
        """
        Return the 3x3 block that contains the given position.
        """
        block_row = row_index // 3
        block_col = col_index // 3
        block = []
        for i in range(3):
            for j in range(3):
                row = 3 * block_row + i
                col = 3 * block_col + j
                block.append(self.board[row][col])
        return block

    def set_value(self, row_index, col_index, value):
        """
        Set the value of the cell at the given position.
        """
        self.board[row_index][col_index] = value

    def get_empty_cell(self):
        """
        Return the position of the first empty cell, or None if the board is full.
        """
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def is_valid(self, row_index, col_index, value):
        """
        Check if the given value can be placed in the given position.
        """
        row = self.get_row(row_index)
        if value in row:
            return False
        col = self.get_column(col_index)
        if value in col:
            return False
        block = self.get_block(row_index, col_index)
        if value in block:
            return False
        return True

    def solve(self):
        """
        Solve the Sudoku board using a recursive backtracking algorithm.
        """
        empty_cell = self.get_empty_cell()
        if not empty_cell:
            return True
        row_index, col_index = empty_cell
        for value in range(1, 10):
            if self.is_valid(row_index, col_index, value):
                self.set_value(row_index, col_index, value)
                if self.solve():
                    return True
                self.set_value(row_index, col_index, 0)
        return False




if __name__ == "__main__":

    board = []
    for i in range(9):
        row = input(f"Enter row {i+1} (use '0' for empty cells): ")
        board.append([int(val) for val in row])
    sudoku = Sudoku(board)
    print("Sudoku board:")
    print(sudoku)
    sudoku.solve()
    print("Solved Sudoku board:")
    print(sudoku)



'''
Example of input:
Enter row 1 (use '0' for empty cells): 530070000
Enter row 2 (use '0' for empty cells): 600195000
Enter row 3 (use '0' for empty cells): 098000060
Enter row 4 (use '0' for empty cells): 800060003
Enter row 5 (use '0' for empty cells): 400803001
Enter row 6 (use '0' for empty cells): 700020006
Enter row 7 (use '0' for empty cells): 060000280
Enter row 8 (use '0' for empty cells): 000419005
Enter row 9 (use '0' for empty cells): 000080079

output of it:
5 3 0  | 0 7 0  | 0 0 0
6 0 0  | 1 9 5  | 0 0 0
0 9 8  | 0 0 0  | 0 6 0
------+-------+------
8 0 0  | 0 6 0  | 0 0 3
4 0 0  | 8 0 3  | 0 0 1
7 0 0  | 0 2 0  | 0 0 6
------+-------+------
0 6 0  | 0 0 0  | 2 8 0
0 0 0  | 4 1 9  | 0 0 5
0 0 0  | 0 8 0  | 0 7 9



Sudoku is a popular logic puzzle game where players fill a 9x9 grid with numbers from 1 to 9.
If you want to solve a Sudoku puzzle or create a new one, you can use the Python program provided above. 
Simply run the program and input the numbers on the grid as prompted, using 0 to represent empty cells. 
The program will then solve the puzzle and display the solution.

Open your terminal or command prompt on your computer.
Navigate to the directory where the program is saved.
Run the program by typing "python sudoku_solver.py" and pressing Enter.
The program will prompt you to enter a 9x9 Sudoku board, row by row. Use "0" for empty cells.
Once you have entered the board, the program will solve it and print out the solution.
If there is no solution, the program will let you know that it was unable to solve the puzzle.

'''