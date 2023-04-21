import argparse
from GridWorld import draw_world

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A* Algorithm Start!")
    parser.add_argument("--M", type=int, default=30, help="Number of rows")
    parser.add_argument("--N", type=int, default=30, help="Number of columns")
    parser.add_argument("--inc_obstacle_ratio", type=float, default=0.2, help="Ratio of obstacle")
    args = parser.parse_args()

    draw_world(args.M, args.N, args.inc_obstacle_ratio)