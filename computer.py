
class Computer:

    verbs = {"open", "look"}

    def __init__(self):
        pass

    def processString(self,string,screen):
        words = string.split()
        if len(words) != 2:
            return 1
        if words[0] in self.verbs:
            verb = words[0]
            if words[1] in screen.getScreenObjects():
                object = words[1]
                screen.processAction(verb,object)

