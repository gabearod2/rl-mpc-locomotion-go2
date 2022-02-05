
class Parameters:
    # def __init__(self):
    #     self.cmpc_x_drag = 3.0
    #     self.cmpc_gait = 9
    #     self.cmpc_bonus_swing = 0.0
    #     self.controller_dt = 0.001
    #     self.count_mpc_time = True

    cmpc_x_drag = 3.0
    cmpc_gait = 9
    cmpc_bonus_swing = 0.0
    cmpc_horizons = 10
    cmpc_weights = [0.25, 0.25, 10, 2, 2, 50, 0, 0, 0.3, 0.2, 0.2, 0.1]
    cmpc_alpha = 4e-5
    controller_dt = 0.002
    cmpc_solver_time = True
