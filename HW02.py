from collections import deque

# Define the capacities of the jugs
capacity_12 = 12
capacity_8 = 8
capacity_3 = 3

# Initial state: all jugs are empty
initial_state = (0, 0, 0)

# Goal state: any jug has exactly 1 liter of water
goal_amount = 1

# Function to get all possible next states from the current state
def get_next_states(state):
    x, y, z = state
    next_states = []
    
    # Fill each jug
    if x < capacity_12:
        next_states.append((capacity_12, y, z))
    if y < capacity_8:
        next_states.append((x, capacity_8, z))
    if z < capacity_3:
        next_states.append((x, y, capacity_3))
    
    # Empty each jug
    if x > 0:
        next_states.append((0, y, z))
    if y > 0:
        next_states.append((x, 0, z))
    if z > 0:
        next_states.append((x, y, 0))
    
    # Pour water from one jug to another
    if x > 0 and y < capacity_8:
        transfer = min(x, capacity_8 - y)
        next_states.append((x - transfer, y + transfer, z))
    if x > 0 and z < capacity_3:
        transfer = min(x, capacity_3 - z)
        next_states.append((x - transfer, y, z + transfer))
    if y > 0 and x < capacity_12:
        transfer = min(y, capacity_12 - x)
        next_states.append((x + transfer, y - transfer, z))
    if y > 0 and z < capacity_3:
        transfer = min(y, capacity_3 - z)
        next_states.append((x, y - transfer, z + transfer))
    if z > 0 and x < capacity_12:
        transfer = min(z, capacity_12 - x)
        next_states.append((x + transfer, y, z - transfer))
    if z > 0 and y < capacity_8:
        transfer = min(z, capacity_8 - y)
        next_states.append((x, y + transfer, z - transfer))
    
    return next_states

# BFS to find all ways to reach the goal
def bfs_all_paths(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)
    goal_paths = []

    while queue:
        current_state, path = queue.popleft()
        x, y, z = current_state

        # Check if we reached the goal
        if x == goal_amount or y == goal_amount or z == goal_amount:
            goal_paths.append(path + [current_state])
            continue

        # Explore the next states
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))

    return goal_paths

# Find all paths to the solution
all_paths = bfs_all_paths(initial_state)
print("Number of ways to reach the goal:", len(all_paths))
for path in all_paths:
    print(path)
