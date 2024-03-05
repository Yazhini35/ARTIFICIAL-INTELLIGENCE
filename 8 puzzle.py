import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
    
    def __lt__(self, other):
        return self.cost < other.cost
    
    def __eq__(self, other):
        return self.state == other.state
    
    def __hash__(self):
        return hash(str(self.state))

class EightPuzzleSolver:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        
    def get_blank_position(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return (i, j)
    
    def generate_children(self, node):
        children = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        
        i, j = self.get_blank_position(node.state)
        for di, dj in directions:
            new_i, new_j = i + di, j + dj
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [row[:] for row in node.state]
                new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                children.append(PuzzleNode(new_state, parent=node, move=(new_i, new_j), depth=node.depth + 1, cost=node.depth + 1 + self.heuristic(new_state)))
        return children
    
    def heuristic(self, state):
        
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    goal_i, goal_j = divmod(state[i][j] - 1, 3)
                    distance += abs(i - goal_i) + abs(j - goal_j)
        return distance
    
    def solve(self):
        open_list = []
        closed_list = set()
        
        initial_node = PuzzleNode(self.initial_state)
        heapq.heappush(open_list, initial_node)
        
        while open_list:
            current_node = heapq.heappop(open_list)
            if current_node.state == self.goal_state:
                path = []
                while current_node:
                    path.append(current_node.state)
                    current_node = current_node.parent
                return path[::-1]
            
            closed_list.add(current_node)
            
            children = self.generate_children(current_node)
            for child in children:
                if child not in closed_list:
                    heapq.heappush(open_list, child)
        
        return None
initial_state = [[1, 2, 3],
                 [4, 0, 5],
                 [6, 7, 8]]

goal_state = [[1, 2, 3],
              [4, 5, 0],
              [6, 7, 8]]

solver = EightPuzzleSolver(initial_state, goal_state)
solution = solver.solve()
if solution:
    print("Solution found:")
    for state in solution:
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
