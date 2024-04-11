import sys

def generate_solutions(row, column):
    """
    solve a simple N x N matrix
    Args:
        row (int): Number of rows
        column (int): Number of columns
    Returns:
        returns a list of lists
    """
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution


def place_queen(queen, column, prev_solution):
    """
    Place the queen at a certain position
    Args:
        queen (int): The queen
        column (int): The column to move
        prev_solution (list): the previous move
    Returns:
        returns a list
    """
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    """
    check if it's safe to make a move
    Args:
        q (int): row to move to
        x (int): column to move to
        array (array): the matrix
    Returns:
        returns a boolean
    """
    if x in array:
        return (False)
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def n_queens(N):
    """
    The main entry point
    Args:
        N (int): The board size (N x N)
    Returns:
        returns None
    """
    solutions = generate_solutions(N, N)
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    n_queens(N)
