# Target Tracking Urban Environment Simulator

This repository contains code for urban environment simulator that can be used to test Target Tracking algorithms. It has functionalities for dynamic target and cylindrical obstacles. 

This work is a part of paper "UAV Target Tracking in Urban Environments using Deep Reinforcement Learning" published at The 2020 International Conference on Unmanned Aircraft Systems, Athens, Greece. In case you find any of this useful consider citing our work.

Preprint will be available shortly!

---

## Contents

- `animation_2d.py`: Simulate the environment in x-y plane.
- `animation_3d.py`: Simulate the environment in x-z plane.
- `create_map.py`: Create customisable map for the environment. 
- `args.py`: Arguments that are used by all other scripts.

## Testing your Algorithms using this Simulator

- Install all required libraries. For this simply run the following command.
```
pip install -r requirements.txt
```

- Add your target-tracking algorithm code in the same directory. 

That file must read the current state of the target from the file `state_car.txt`, which could be used to determine the effectiveness of the choosen action by your algotithm. You may use the snippet given below for reading the file.

```
file = open("state_car.txt", "r")
car_state = file.read().split()
car_state = list(map(float, car_state))
```

It also must write the state of the drone obtained by performing the action suggested by your algorithm. You could use the following snippet for that. Here, `time_step_drone` is the step counter which is incremented whenever an action is taken by the agent.

```
file = open("state_drone.txt", "w")
file.write(str(state_x) + ' ' + str(state_y) + ' ' + str(state_z) + ' ' + str(time_step_drone))
file.close()
```

- Change the position, radius, height and number of obstacles based on your requirements. This can be done by changing line 44-46 in `animation_2d.py` and line 45-47 in `animation_3d.py`. 

For example, for setting the position as p_x and p_y, radius as r and height as h for an obstacle, make the following additions to `animation_2d.py` and `animation_3d.py` respectively.

```
obstacle_name = patches.Circle((p_x, p_y), radius=r, fc='g')

obstacle_name = patches.Rectangle((p_x, 0), 2*r, h, fc='g') 
```

We could also change the field of view of the agent (<i>FOV</i>) by changing line 59 in `animation_2d.py`. Say, we want to make the radius of field of view as fov_radius, just make the following change.

```
fov_circle = patches.Circle((0, 0), radius=fov_radius, fc=None, ec='k', alpha=0.3)
```

- Add or change the arguments of your choice in `args.py` file. You may also want to change the plotting configurations placed immediately after the import statements in all animation files.

- Finally, for simulating an episode using actions suggested by your algorithm, run the following commands in seperate terminals.

```
python animation_2d.py
python animation_3d.py
python your_target_tracking_algorithm_script.py
```

## Screenshot of Environment

Below is a screenshot of the environment developed by the `animation_2d.py` script. Here, red circle depicts the agent, yellow circle depicts the target, blue circle depicts the <i>FOV</i> and green ones depict the obstacles.

![figure](environment.png)

---
### Contact

If you face any problem in running this code, you can contact us at sarthak16189@iiitd.ac.in.

### License

Copyright (c) 2020 Sarthak Bhagat, P.B. Sujit. 

For license information, see LICENSE or http://mit-license.org


