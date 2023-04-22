import argparse
from GridWorld import draw_world

##################################예외처리 구현 필요
# global window_size, grid_world_size
# wind
# grid_world_size = (600, 600)
# min_cell_size = 10
#
# max_rows = grid_world_size[0] // min_cell_size
# max_cols = grid_world_size[1] // min_cell_size
#
# def limited_int(x, max_value):
#     x = int(x)
#     if x < 1 or x > max_value:
#         raise argparse.ArgumentTypeError(f"Value must be between 1 and {max_value}, but got {x}")
#     return x
#
# def limited_rows(x):
#     return limited_int(x, max_rows)
#
# def limited_cols(x):
#     return limited_int(x, max_cols)
#
# def limited_float(x, max_value):
#     if x < 0 or x > 0.95:
#         raise argparse.ArgumentTypeError(f"Value must be between 0 and 0.95, but got {x}")
#     return x


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A* Algorithm Start!")
    parser.add_argument("--M", type=int, default=30, help="Number of rows")
    parser.add_argument("--N", type=int, default=30, help="Number of columns")
    parser.add_argument("--inc_obstacle_ratio", type=float, default=0.2, help="Ratio of obstacle")
    args = parser.parse_args()

    draw_world(args.M, args.N, args.inc_obstacle_ratio)