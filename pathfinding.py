from queue import Queue, LifoQueue, PriorityQueue

def bfs(start_node, target_node):
    visited = set()
    queue = Queue()
    queue.put((start_node, [start_node]))

    while not queue.empty():
        current, path = queue.get()
        if current == target_node:
            return path
        visited.add(current)
        for neighbor in current.neighbors.values():
            if neighbor not in visited and neighbor is not None:
                queue.put((neighbor, path + [neighbor]))
    return []

def dfs(start_node, target_node):
    visited = set()
    stack = LifoQueue()
    stack.put((start_node, [start_node]))

    while not stack.empty():
        current, path = stack.get()
        if current == target_node:
            return path
        visited.add(current)
        for neighbor in current.neighbors.values():
            if neighbor not in visited and neighbor is not None:
                stack.put((neighbor, path + [neighbor]))
    return []

def heuristic(node_a, node_b):
    # Simple Manhattan distance heuristic
    return abs(node_a.position.x - node_b.position.x) + abs(node_a.position.y - node_b.position.y)

def a_star(start_node, target_node):
    open_set = PriorityQueue()
    open_set.put((0, start_node))
    came_from = {}
    g_score = {start_node: 0}
    f_score = {start_node: heuristic(start_node, target_node)}
    visited = set()

    while not open_set.empty():
        _, current = open_set.get()
        if current == target_node:
            return reconstruct_path(came_from, current)
        visited.add(current)
        for neighbor in current.neighbors.values():
            if neighbor is None or neighbor in visited:
                continue
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, target_node)
                open_set.put((f_score[neighbor], neighbor))
    return []

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path
