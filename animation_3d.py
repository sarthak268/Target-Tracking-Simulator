import matplotlib
matplotlib.use('TKAgg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import animation
import random
import math
import pickle
from args import FLAGS

fig = plt.figure()
plt.axis('equal')
plt.grid()
ax = fig.add_subplot(111)
ax.set_xlim(-25, 125)
ax.set_ylim(-25, 125)
ax.set_xticks(np.arange(-25, 126, 25))
ax.set_yticks(np.arange(-25, 126, 25))

car = patches.Rectangle((0, 0), 0, 0, fc='y')
car.set_width(7.5)
car.set_height(7.5)

drone = patches.Rectangle((0, 0), 0, 0, fc='r')
drone.set_width(5)
drone.set_height(5)

current_x = 0
current_y = 0

current_x_drone = 0
current_y_drone = 0

drone_dir_x = 0
drone_dir_y = 0

current_x_car = 0
current_y_car = 0

car_dir_x = 0
car_dir_y = 0

################ adding obstacles
obstacle1 = patches.Rectangle((30, 0), 5, 50, fc='g')
obstacle2 = patches.Rectangle((20, 0), 5, 50, fc='g')
obstacle3 = patches.Rectangle((50, 0), 10, 50, fc='g') 

def distance(x1, y1, x2, y2):
	return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def get_direction_given():
	file = open("state_drone.txt", "r")
	move_to = file.read().split()
	if (len(move_to) > 0):
		return float(move_to[0]), float(move_to[1]), float(move_to[2])
	else:
		return 0.0, 0.0, 0.0

def get_direction_given_car():
	file = open("state_car.txt", "r")
	move_to = file.read().split()
	if (len(move_to) > 0):
		return float(move_to[0]), float(move_to[1])
	else:
		return 0.0, 0.0 

def move_drone(drone_dir_x, drone_dir_y, speed):
	global current_x_drone
	global current_y_drone
	# here y represents height of drone (conventionally z)
	
	if (distance(current_x_drone, current_y_drone, drone_dir_x, drone_dir_y) >= 1):
		theta = math.atan2((drone_dir_y - current_y_drone) , (drone_dir_x - current_x_drone + 0.000001))
		next_x = current_x_drone + speed*math.cos(theta)
		next_y = current_y_drone + speed*math.sin(theta)
	else:
		next_x = current_x_drone
		next_y = current_y_drone

	drone.set_xy([next_x, next_y])
	
	current_x_drone = next_x
	current_y_drone = next_y
	return drone

def move_car(car_dir_x, car_dir_y, speed):
	global current_x_car
	
	theta = math.atan2((car_dir_y - current_y_car) , (car_dir_x - current_x_car + 0.000001))
	next_x = current_x_car + speed*math.cos(theta)
	
	car.set_xy([next_x, 0])
	
	current_x_car = next_x
	return car	

def init():
    ax.add_patch(car)
    ax.add_patch(drone)
    ax.add_patch(obstacle1)
    ax.add_patch(obstacle2)
    ax.add_patch(obstacle3)
    return car, drone,

def animate(i):
	global move_dir_x_drone
	global move_dir_y_drone
	global move_dir_x_car
	global move_dir_y_car

	# for car
	speed_car = 1.0
	move_dir_x_car, move_dir_y_car = get_direction_given_car()
	c = move_car(move_dir_x_car, move_dir_y_car, speed_car)

	# for drone
	speed_drone = 1.0
	move_dir_x_drone, move_dir_y_drone, move_dir_z_drone = get_direction_given()
	d = move_drone(move_dir_x_drone, move_dir_z_drone, speed_drone)

	return c, d,

def main_animation():
	# anim = animation.FuncAnimation(fig, animate,
	# 							   init_func=init,
	# 							   frames=1000,
	# 							   interval=500,
	# 							   blit=False)
	anim = animation.FuncAnimation(fig, animate,
								   init_func=init,
								   frames=20,
								   interval=500,
								   blit=False)
	#anim.save('movie.gif', writer='imagemagick')
	plt.title('X-Z Plot')
	plt.xlabel('X')
	plt.ylabel('Z')
	plt.show()
	
if (__name__ == '__main__'):
	main_animation()
