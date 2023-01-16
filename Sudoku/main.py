import numpy as np

grid = [[0, 0, 0, 8, 3, 0, 0, 5, 7],
        [0, 0, 8, 5, 0, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 2, 0, 8, 0],
        [8, 0, 2, 3, 9, 0, 7, 0, 0],
        [6, 0, 0, 1, 0, 0, 0, 3, 2],
        [0, 5, 7, 2, 0, 4, 0, 9, 0],
        [0, 6, 0, 4, 1, 0, 3, 7, 0],
        [0, 7, 3, 9, 0, 8, 0, 6, 0],
        [0, 0, 0, 7, 6, 0, 4, 0, 0]]


def possible(row, column, number):
        global grid

        # Is the number appearing in the row?
        for i in range(0, 9):
                if grid[row][i] == number:
                        return False
        # Is the number appearing in the column?
        for i in range(0, 9):
                if grid[i][column] == number:
                        return False

        # Is the number appearing in the square?
        x0 = (column // 3) * 3
        y0 = (row // 3) * 3
        for i in range(0, 3):
                for j in range(0, 3):
                        if grid[y0 + i][x0 + j] == number:
                                return False

        return True


def solve():
        global grid
        for row in range(0, 9):
                for column in range(0, 9):
                        if grid[row][column] == 0:
                                for number in range (1, 10):
                                        if possible(row, column, number):
                                                grid[row][column] = number
                                                solve()
                                                grid[row][column] = 0

                                return


        print(np.matrix(grid))
        input("More possible solutions")

solve()





