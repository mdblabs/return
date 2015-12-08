
class Screen:
    objects = {}
    states = {}
    transitions = {}

    def __init__(self,objectsList,states,transitions):
        self.inScreen = True
        self.objects = objectsList
        self.states = states
        self.transitions = transitions

    def processAction(self,verb,object):
        actualState = self.getState()
        if verb in self.transitions:
            if object in self.transitions[verb]:
                if actualState in self.transitions[verb]:
                    self.setState(self.transitions[verb][2])
                #TODO:Manage exceptions


    def getState(self):
        for state in self.states:
            if 1 in state:
                return state[0]

    def setState(self,state):
        actualState = self.getState()
        for st in self.states:
            if state in st and st[1]==0:
                st[1]=1
        for st in self.states:
            if actualState in st and st[1]==1:
                st[1]=0


    def getScreenObjects(self):
        return self.objects

    def getInScreen(self):
        return self.inScreen

    def setInScreen(self,state):
        self.inScreen = state



