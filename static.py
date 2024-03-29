import numpy as np
import pandas as pd 
from corporates import *
from central_bank import *
from banks import *
from arbitragers import *
from speculators import *

# This class to the agent input to the model
class all_agents():
    '''
    Agents to be put into the model
    '''
    def __init__(self):

        self.corporates = [corporate_v0()]
        self.central_banks = [central_bank_v0()]
        self.banks = [local_bank()]
        self.arbitragers = [arbitrager()]
        self.speculators = [speculator()]

        
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

class arbitrager():
    '''
    To specify arbitragers
    '''
    def __init__(self):
        self.name = 'Arbitrager'
        self.params = params_arbitrager()
        self.agent = agent_arbitrager

class speculator():
    '''
    To specify speculators
    '''
    def __init__(self):
        self.name = 'Speculator'
        self.params = params_speculator()
        self.agent = agent_speculator
        

# This section is to set the hyperparameters of each type of agent
class params_corporate_v0():
    '''
    parameters for a corporate agent
    '''
    def __init__(self):
        self.init_population = 200
        self.country = ["A", "B"]
        self.asset_min = 100
        self.asset_max = 200
        self.costs_min = 5
        self.costs_max = 10
        self.level_min = 1
        self.level_max = 5
        
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

        self.init_pos = [(13,3), (3,3), (10,51), (23,44),  # US Bank 
                         (16, 67), (15, 71), (15, 67), (7,73)] # JP Bank
        self.local_asset_min = 12000
        self.local_asset_max = 25000
        self.local_costs_min = 20
        self.local_costs_max = 25
        self.foreign_asset_min = 7000
        self.foreign_asset_max = 12000
        self.foreign_costs_min = 15
        self.foreign_costs_max = 20
        self.vision_min = 50
        self.vision_max = 50
        
class params_international_bank():
    '''
    parameters for an international bank
    '''
    def __init__(self):
        self.init_pos = [(16, 7), (10, 71)] 
        self.local_asset_min = 2000
        self.local_asset_max = 4000
        self.local_costs_min = 24
        self.local_costs_max = 40
        self.foreign_asset_min = 1000
        self.foreign_asset_max = 2000
        self.foreign_costs_min = 12
        self.foreign_costs_max = 20
        self.vision_min = 100
        self.vision_max = 100
        
class params_arbitrager():
    '''
    parameters for a arbitrager
    '''
    def __init__(self):
        self.init_pos = [(24,15), (24,35), (24, 50), (24, 75)]
        self.asset_min = 25000
        self.asset_max = 25000
        self.costs_min = 1
        self.costs_max = 2
        self.vision_min = 100
        self.vision_max = 100
        
class params_speculator():
    '''
    parameters for a speculator
    '''
    def __init__(self):
        self.init_pos = [(15,46), (15,70), (14,46), (10,50), (25,42), (13, 65), (22, 40), (16, 63), (13, 64)]
        self.strategies = ['mean revert', 'mean revert', 'uncoveredIR', 'momentum', 'mean revert', 'uncoveredIR', 'mean revert', 'mean revert', 'momentum']
        self.asset_min = 10000 / 2
        self.asset_max = 12000 / 2
        self.costs_min = 1
        self.costs_max = 1


# This section is to store maps in form of arrays      
class static_map_v0():
    '''
    A customed static map for init
    '''
    def __init__(self):

        us_map = pd.read_excel(r"../ABM_FX/geographic_data/MAP.xlsx", sheet_name = "US_MAP").values
        jp_map = pd.read_excel(r"../ABM_FX/geographic_data/MAP.xlsx", sheet_name = "JP_MAP").values

        self.width = us_map.shape[0]
        self.height = us_map.shape[1]

        adj_us_map = []
        for i in range(us_map.shape[0]):
            for j in range(us_map.shape[1]):
                if j < 60:
                    adj_us_map.append(us_map[i][j] * 10)
                else:
                    adj_us_map.append(us_map[i][j] * 10)
        adj_us_map = np.array(adj_us_map).reshape(us_map.shape)
                
        
        adj_jp_map = []
        for i in range(us_map.shape[0]):
            for j in range(us_map.shape[1]):
                if j > 60:
                    adj_jp_map.append(jp_map[i][j] * 14)
                else:
                    adj_jp_map.append(jp_map[i][j] * 14)
        adj_jp_map = np.array(adj_jp_map).reshape(us_map.shape)
                    
            
        self.currencyA_map_init = adj_us_map
        self.currencyB_map_init = adj_jp_map