from MPC_Controller.FSM_states.ControlFSMData import ControlFSMData
from MPC_Controller.FSM_states.FSM_State import FSM_State, FSM_StateName


class FSM_State_Passive(FSM_State):
    def __init__(self, _controlFSMData: ControlFSMData):
        super().__init__(_controlFSMData, FSM_StateName.PASSIVE, "PASSIVE")