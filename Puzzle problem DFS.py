TARGET_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def locate_blank_tile(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

def swap_tiles(puzzle, x1, y1, x2, y2):
    updated_puzzle = [row[:] for row in puzzle]
    updated_puzzle[x1][y1], updated_puzzle[x2][y2] = updated_puzzle[x2][y2], updated_puzzle[x1][y1]
    return updated_puzzle

def dfs_solver(start_puzzle):
    stack = [(start_puzzle, [])]
    explored_states = set()

    while stack:
        current_puzzle, steps = stack.pop()
        explored_states.add(tuple(map(tuple, current_puzzle)))

        if current_puzzle == TARGET_STATE:
            return steps

        x, y = locate_blank_tile(current_puzzle)
        possible_moves = []
        if x > 0: possible_moves.append(swap_tiles(current_puzzle, x, y, x-1, y))
        if x < 2: possible_moves.append(swap_tiles(current_puzzle, x, y, x+1, y))
        if y > 0: possible_moves.append(swap_tiles(current_puzzle, x, y, x, y-1))
        if y < 2: possible_moves.append(swap_tiles(current_puzzle, x, y, x, y+1))

        for new_puzzle in possible_moves:
            if tuple(map(tuple, new_puzzle)) not in explored_states:
                stack.append((new_puzzle, steps + [new_puzzle]))

    return None

def get_user_puzzle():
    print("Enter the initial state of your 8-puzzle (use 0 for the blank):")
    puzzle = []
    for i in range(3):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        puzzle.append(row)
    return puzzle

start_state = get_user_puzzle()
solution_path = dfs_solver(start_state)

if solution_path:
    print("Solution found using DFS!")
    for step in solution_path:
        for row in step:
            print(row)
        print()
else:
    print("No solution could be found.")
