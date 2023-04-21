from Astar import Astar

if __name__ == '__main__':
    arr = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0]
]

    start = (0, 0)
    end = (4, 4)

    # 0 - manhattan, 1 - euclidean
    heuristic_function = 1

    model = Astar(arr, start, end, heuristic_function)
    path, explored_nodes = model.get_path()

    print("PATH:", path)
    print("Explored nodes:", explored_nodes)