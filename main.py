import argparse
from GridWorld import draw_world

def check_mn(value):
    ivalue = int(value)
    if ivalue < 10 or ivalue > 60:
        raise argparse.ArgumentTypeError("M and N must be between 2 and 60")
    return ivalue

def check_inc_obstacle_ratio(value):
    fvalue = float(value)
    if fvalue <= 0 or fvalue > 0.95:
        raise argparse.ArgumentTypeError("inc_obstacle_ratio must be between 0 and 0.95 (exclusive)")
    return fvalue

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A* Algorithm Start!")
    parser.add_argument("--M", type=check_mn, default=30, help="Number of rows")
    parser.add_argument("--N", type=check_mn, default=30, help="Number of columns")
    parser.add_argument("--inc_obstacle_ratio", type=check_inc_obstacle_ratio, default=0.2, help="Ratio of obstacle")
    args = parser.parse_args()

    draw_world(args.M, args.N, args.inc_obstacle_ratio)