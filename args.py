import argparse

parser = argparse.ArgumentParser(description='RL agents for target tracker')
    
parser.add_argument("--state_space_dim", type=int, default=101*101*11, help="dimension of state space")
parser.add_argument("--grid_size", type=int, default=101, help="size of grid")
parser.add_argument("--action_space_dim", type=int, default=6, help="dimension of action space")
parser.add_argument("--height_levels", type=int, default=11, help="number of discrete height levels")

FLAGS = parser.parse_args() 

