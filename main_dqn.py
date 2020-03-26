import argparse
from target_tracking_algo import *

def main():
    parser = argparse.ArgumentParser(description='RL agents for target tracker')
    
    parser.add_argument("--state_space_dim", type=int, default=101*101*11, help="dimension of state space")
    parser.add_argument("--grid_size", type=int, default=101, help="size of grid")
    parser.add_argument("--action_space_dim", type=int, default=6, help="dimension of action space")
    parser.add_argument("--height_levels", type=int, default=11, help="number of discrete height levels")
    parser.add_argument("--min_height_threshold", type=float, default=20.0, help="minimum possible height for the drone")

    # add rest of the arguments for 

    FLAGS = parser.parse_args()

    return FLAGS

if (__name__ == '__main__'):
	
    flags = main()
    target_tracker(flags)
