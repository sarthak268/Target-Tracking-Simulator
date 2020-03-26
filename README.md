# Target Tracking Simulator

This repository contains code for urban environment simulator that can be used to test Target Tracking algorithms. It has functionalities for dynamic target and cylindrical obstacles.

### Testing your algoriths using this simulator

- Add your target-tracking algorithm code in the same directory. 

That file must read the current state of the target from the file <i>state_car.txt</i>, which could be used to determine the effectiveness of the choosen action by your algotithm. You amy use the snippet given below for reading the file.

```
file = open("state_car.txt", "r")
car_state = file.read().split()
car_state = list(map(float, car_state))
```

It also must write the state of the drone obtained by performing the action suggested by your algorithm. You could use the following snippet for that. Here, <i>time_step_drone</i> is the step counter which is incremented whenever an action is taken by the agent.

```
file = open("state_drone.txt", "w")
file.write(str(state_x) + ' ' + str(state_y) + ' ' + str(state_z) + ' ' + str(time_step_drone))
file.close()
```
- Add or change the arguments of your choice in <i>args.py</i> file. You may also want to change the plotting configurations placed immediately after the import statements in all animation files.
