# Target Tracking Simulator

This repository contains code for urban environment simulator that can be used to test Target Tracking algorithms. It has functionalities for dynamic target and cylindrical obstacles.

## Testing your algoriths using this simulator

- Add your target-tracking algorithm code in the same directory. That file must read the current state of the target from the file <i>state_car.txt</i>, which could be used to determine the effectiveness of the choosen action by your algotithm. 

```
file = open("state_car.txt", "r")
car_satte = file.read().split()
car_Satte = list(map(float, car_state))
```

It also must write the state of the 
