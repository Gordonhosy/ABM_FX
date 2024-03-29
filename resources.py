import mesa

class currencyA_basic(mesa.Agent):
    '''
    Currency A:
    - the block contains currency A to be earned
    - currency A grows at a rate of 1
    '''
    
    def __init__(self, agent_id, model, pos, max_dollar):
        super().__init__(agent_id, model)
        self.pos = pos
        self.amount = max_dollar
        self.max_dollar = max_dollar
        self.base_growth = 0.3
        
    def step(self, growth_rate):
        '''
        Grows one currency per time step until it reaches maximum
        '''
        self.amount = min([self.max_dollar, self.amount * (1 + self.base_growth +  growth_rate)])
        

class currencyB_basic(mesa.Agent):
    '''
    Currency B:
    - the block contains currency B to be earned
    - currency B grows at a rate of 1
    '''
    
    def __init__(self, agent_id, model, pos, max_dollar):
        super().__init__(agent_id, model)
        self.pos = pos
        self.amount = max_dollar * 100
        self.max_dollar = max_dollar * 100
        self.base_growth = 0.3
        
    def step(self, growth_rate):
        '''
        Grows one currency per time step until it reaches maximum
        '''
        self.amount = min([self.max_dollar, self.amount * (1 + self.base_growth + growth_rate)])    