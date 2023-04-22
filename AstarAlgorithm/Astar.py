from heapq import heappush, heappop
from AstarAlgorithm.distance_functions import compute_manhattan_distance, compute_euclidean_distance
from AstarAlgorithm.Node import Node

class Astar:

    def __init__(self, arr, start, end, heuristic_function):
        self.arr = arr
        self.start = start
        self.end = end
        self.heuristic_fucntion = heuristic_function



    def get_neighbors(self, arr, node):
        node_list = []
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            x, y = node.get_position()

            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]):
                if arr[nx][ny] != 'X':
                    node_list.append(Node((nx, ny), node))
        return node_list

    def compute_distance(self, a, b):
        if self.heuristic_fucntion:
            return compute_euclidean_distance(a, b)
        return compute_manhattan_distance(a, b)


    def get_path(self):
        start_node = Node(self.start, g=0, h=self.compute_distance(self.start, self.end))
        end_node = Node(self.end)

        path = []

        open_list = []
        close_list = []

        heappush(open_list, start_node)
        while open_list:
            current_node = heappop(open_list)
            close_list.append(current_node)

            if current_node == end_node:
                while current_node is not None:
                    path.append(current_node.get_position())
                    current_node = current_node.get_parent()
                return path[::-1], len(close_list)

            neighbors = self.get_neighbors(self.arr, current_node)

            for neighbor in neighbors:
                if neighbor not in close_list:
                    tmp_g = neighbor.get_g()
                    next_g = tmp_g + 1  # 거리 비용 1

                    if neighbor not in open_list or next_g < tmp_g:
                        neighbor.set_parent(current_node)
                        neighbor.set_g(next_g)
                        neighbor.set_h(self.compute_distance(neighbor.get_position(), end_node.get_position()))
                        neighbor.set_f(neighbor.get_g() + neighbor.get_h())

                        if neighbor not in open_list:
                            heappush(open_list, neighbor)

        if not path:
            lowest_f_node = min(close_list, key=lambda node: node.get_f())
            best_path = []

            while lowest_f_node is not None:
                best_path.append(lowest_f_node.get_position())
                lowest_f_node = lowest_f_node.get_parent()

            return best_path[::-1], len(close_list)