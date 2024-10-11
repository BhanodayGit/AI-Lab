TARGET_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def locate_blank(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

def swap_tiles(puzzle, x1, y1, x2, y2):
    modified_puzzle = [row[:] for row in puzzle]
    modified_puzzle[x1][y1], modified_puzzle[x2][y2] = modified_puzzle[x2][y2], modified_puzzle[x1][y1]
    return modified_puzzle

def bfs_solver(initial):
    queue = [(initial, [])]
    visited_states = set()
    while queue:
        current_state, steps = queue.pop(0)
        visited_states.add(tuple(map(tuple, current_state)))

        if current_state == TARGET_STATE:
            return steps

        x, y = locate_blank(current_state)
        possible_moves = []
        if x > 0: possible_moves.append(swap_tiles(current_state, x, y, x-1, y))
        if x < 2: possible_moves.append(swap_tiles(current_state, x, y, x+1, y))
        if y > 0: possible_moves.append(swap_tiles(current_state, x, y, x, y-1))
        if y < 2: possible_moves.append(swap_tiles(current_state, x, y, x, y+1))

        for new_state in possible_moves:
            if tuple(map(tuple, new_state)) not in visited_states:
                queue.append((new_state, steps + [new_state]))

    return None

def get_user_input():
    print("Enter the initial state of the 8-puzzle (0 for blank):")
    puzzle = []
    for i in range(3):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        puzzle.append(row)
    return puzzle

start_state = get_user_input()
solution_path = bfs_solver(start_state)

if solution_path:
    print("Solution found using BFS!")
    for step in solution_path:
        for row in step:
            print(row)
        print()
else:
    print("No solution could be found.")
