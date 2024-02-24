import numpy as np
from corporates import *
from central_bank import *
from banks import *

# This class to the agent input to the model
class all_agents():
    '''
    Agents to be put into the model
    '''
    def __init__(self):

        self.corporates = [corporate_v0()]
        self.central_banks = [central_bank_v0()]
        self.banks = [local_bank(), international_bank()]
        # TO DO: include different types of agents here

        
# This section is to specify a complete agent type from: agent type + parameters
class corporate_v0():
    '''
    To specify corporate version 0
    '''
    def __init__(self):
        self.name = 'Corporate V0'
        self.params = params_corporate_v0()
        self.agent = agent_corporate_v0

class central_bank_v0():
    '''
    To specify central bank version 0
    '''
    def __init__(self):
        self.name = 'Central Bank V0' # name of the agent 
        self.params = params_central_bank_v0() # parameters setting for central bank
        self.agent = agent_central_bank_v0 # general agent model for central bank

class local_bank():
    '''
    To specify local bank
    '''
    def __init__(self):
        self.name = 'Local Bank'
        self.params = params_local_bank()
        self.agent = agent_bank
        
class international_bank():
    '''
    To specify internatinoal bank
    '''
    def __init__(self):
        self.name = 'International Bank'
        self.params = params_international_bank()
        self.agent = agent_international_bank
        

# This section is to set the hyperparameters of each type of agent
class params_corporate_v0():
    '''
    parameters for a corporate agent
    '''
    def __init__(self):
        self.init_population = 300
        self.asset_min = 25
        self.asset_max = 50
        self.costs_min = 1
        self.costs_max = 5
        self.vision_min = 1
        self.vision_max = 1
        
class params_central_bank_v0():
    '''
    parameter for a central bankS
    '''
    def __init__(self):
        self.number_of_central_bank = 2

class params_local_bank():
    '''
    parameters for a local bank
    '''
    def __init__(self):
        self.init_pos = [(10,10), (20,10), (30,10), (40,10), (10,40), (20,40), (30,40), (40,40)]
        self.local_asset_min = 250
        self.local_asset_max = 500
        self.local_costs_min = 4
        self.local_costs_max = 7
        self.foreign_asset_min = 125
        self.foreign_asset_max = 250
        self.foreign_costs_min = 3
        self.foreign_costs_max = 5
        self.vision_min = 20
        self.vision_max = 20
        
class params_international_bank():
    '''
    parameters for an international bank
    '''
    def __init__(self):
        self.init_pos = [(25, 15), (25,35)]
        self.local_asset_min = 2000
        self.local_asset_max = 4000
        self.local_costs_min = 24
        self.local_costs_max = 40
        self.foreign_asset_min = 1000
        self.foreign_asset_max = 2000
        self.foreign_costs_min = 12
        self.foreign_costs_max = 20
        self.vision_min = 50
        self.vision_max = 50


# This section is to store maps in form of arrays      
# TO DO: a better map
class static_map_v0():
    '''
    A customed static map for init
    '''
    def __init__(self):
        self.width = 50
        self.height = 50
        self.currencyA_map_init = np.array([
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0]
        ])
        self.currencyB_map_init = np.array([
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0],
            [0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0]
        ])
        