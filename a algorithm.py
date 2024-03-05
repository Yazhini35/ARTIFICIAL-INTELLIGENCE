import heapq

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(maze, start, end):
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize open and closed lists
    open_list = []
    closed_list = []

    # Add start node
    heapq.heappush(open_list, (start_node.f, start_node))
    
    # Loop until end is found
    while open_list:
        current_node = heapq.heappop(open_list)[1]

        # Check if goal reached
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            
            # Check if within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0:
                continue
            
            # Check if wall
            if maze[node_position[0]][node_position[1]] != 0:
                continue
            
            # Create new node
            new_node = Node(current_node, node_position)
            children.append(new_node)
        
        # Loop through children
        for child in children:
            # Check if child in closed list
            if child in closed_list:
                continue
            
            # Calculate f, g, h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h
            
            # Check if child in open list and if so, if it has a lower f value
            for _, open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    break
            else:
                # Add child to open list
                heapq.heappush(open_list, (child.f, child))
        
        # Add current node to closed list
        closed_list.append(current_node)
    
    return None

# Example usage
if __name__ == "__main__":
    maze = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    end = (4, 4)

    path = astar(maze, start, end)
    print(path)
