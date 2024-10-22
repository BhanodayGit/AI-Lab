import random

def generate_random_state(n):
    return [random.randint(0, n - 1) for _ in range(n)]

def calculate_cost(state):
    cost = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            # Check if queens are in the same column or on the same diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                cost += 1
    return cost

def generate_neighbours(state):
    neighbours = []
    n = len(state)
    for row in range(n):
        for col in range(n):
            if state[row] != col:
                new_state = state.copy()
                new_state[row] = col
                neighbours.append(new_state)
    return neighbours

def print_chessboard(state):
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[row] == col:
                line += "Q "  # Queen's position
            else:
                line += ". "  # Empty space
        print(line)
    print()

def hill_climbing_n_queens(n):
    current_state = generate_random_state(n)
    current_cost = calculate_cost(current_state)
    step = 1
    
    while True:
        print(f"\nStep {step}:")
        print(f"Current State: {current_state}, Cost: {current_cost}")
        print_chessboard(current_state)
        
        neighbours = generate_neighbours(current_state)
        neighbour_costs = [calculate_cost(neighbour) for neighbour in neighbours]
        best_neighbour_cost = min(neighbour_costs)
        best_neighbour = neighbours[neighbour_costs.index(best_neighbour_cost)]
        
        # Show best neighbour
        print(f"Best Neighbour: {best_neighbour}, Cost: {best_neighbour_cost}")
        print_chessboard(best_neighbour)
        
        if best_neighbour_cost < current_cost:
            current_state = best_neighbour
            current_cost = best_neighbour_cost
        else:
            # If no better neighbour is found, terminate (local minimum)
            print("\nLocal minimum reached, terminating...")
            break
        
        # If we found a solution (cost = 0)
        if current_cost == 0:
            print("\nSolution found!")
            break
        
        step += 1
    
    return current_state, current_cost

n = 4
solution, cost = hill_climbing_n_queens(n)

print(f"\nFinal Solution: {solution}, Cost: {cost}")
print("Final Chessboard:")
print_chessboard(solution)
