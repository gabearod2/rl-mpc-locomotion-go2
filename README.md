# RL MPC Locomotion

## Control Blocks

<img src="images/controller_blocks.png" width=500>


## Blog

- python模仿结构体必须放在__init__()里面，否则无法实例化
- class可以声明确定类型的值为None成员变量

### Structure
```
main_helper() ->
    SimulationBridge ->
        RobotRunner ->
            Quadruped,
            StateEstimatorContainer,
            LegController,
            MIT_Controller ->
                ControlFSM ->
                    FSM_State_Locomotion ->
                        ConvexMPCLocomotion ->
                            convexMPC_interface ->
                                SolverMPC
```
- Not implemented yet:
  - main_helper
  - SimulationBridge
  - RobotRunner

- Partially implemented:
  - StateEstimatorContainer
  - LegController
  - ControlFSM
  - FSM_State_Locomotion

- Fully implemented:
  - ConvexMPCLocomotion
  - convexMPC_interface
  - SolverMPC

## Notes

- [Model Import](docs/0-model_import.md)
- [MIT Cheetah Installation](docs/1-MIT_cheetah_installation.md)

## Gallery

<img src="images/aliengo_static.png" width=500>
<img src="images/aliengo_train.png" width=500>
