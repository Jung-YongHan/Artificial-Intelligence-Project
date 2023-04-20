from heapq import heappush, heappop
from distance_functions import compute_manhattan_distance, compute_euclidean_distance
from Node import Node

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_neighbors(arr, node):
    node_list = []
    for i in range(4):
        x, y = node.get_position()

        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]):
            if arr[nx][ny] != 1:
                node_list.append(Node((nx, ny), node))
    return node_list

def astar(arr, start, end):
    start_node = Node(start, g=0, h=compute_euclidean_distance(start, end))
    end_node = Node(end)

    path = []

    open_list = []
    close_list = []

    heappush(open_list, (start_node.get_f(), start_node))
    while open_list:
        current_node = heappop(open_list)[1]
        close_list.append(current_node)

        if current_node == end_node:
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        neighbors = get_neighbors(arr, current_node)

        for neighbor in neighbors:
            if neighbor not in close_list:
                tmp_g = neighbor.get_g()
                next_g = tmp_g + 1  # 거리 비용 1

                if neighbor not in open_list or next_g < tmp_g:
                    neighbor.set_parent(current_node)
                    neighbor.set_g(next_g)
                    neighbor.set_h(compute_euclidean_distance(neighbor.get_position(), end_node.get_position()))
                    neighbor.set_f(neighbor.get_g() + neighbor.get_h())

                    if neighbor not in open_list:
                        heappush(open_list, (neighbor.get_f(), neighbor))

    print(path)

if __name__ == '__main__':
    arr = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
    astar(arr, (0, 0), (4, 4))