import pygame

pygame.init()

class Screen:
    # TODO: objects must be part of state or player
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
    pass

class State:
    """
    State class.
    Info: Class holder for state interaction and managing.
    Can play one animation, one sound, and take care of objects, present on the scene.
    Interfaces:
    """
    def __init__(self,objectsList,animation,sound):
        self.objects = objectsList
        self.animation = animation
        self.sound = sound
        self. active = False
    pass

    def playAnimation(self):
        """
        Plays animation, depending on activation
        :return:
        """

    def playSound(self):
        """
        Plays a state-related sound, in a loop.
        :return:
        """

    def activate(self):
        """
        Activates state.
        :return:
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates state.
        :return:
        """
        self.active = False

    def getState(self):
        """
        Returns state status.
        :return:
        """
        return self.active



class Animation:
    """
    Animation class.
    Info: Class that implements visual animations
    Interfaces:
    """
    pass


