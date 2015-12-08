import pygame
pygame.init()

class Console:
    fontHeight = 48
    consoleFont = pygame.font.SysFont("monospace", fontHeight)

    # TODO: modify console size to a smaller rectangle, for drawing efficiency.

    consoleScreen = pygame.display.set_mode((1024,768))
    promt = '>'
    letter = ''
    line = promt

    def __init__(self):
        pass

    def update(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.line[:-1]
                    self.consoleScreen.fill((0,0,0))
                    retLine = self.line[1:]
                    self.line=self.promt
                    return retLine
                elif event.key == pygame.K_BACKSPACE:
                    if len(self.line)>1:
                        self.line = self.line[:-1]
                    self.consoleScreen.fill((0,0,0))
                elif event.key == pygame.K_ESCAPE:

                    # TODO: Break gameplay

                    pass
                elif event.key == pygame.K_TAB:

                    # TODO: Nothing?

                    pass
                else:
                    try:
                        self.line+=str(event.unicode)
                        return None
                    except UnicodeEncodeError:
                        print "Error Unicode"
                        pass

        label = self.consoleFont.render(self.line,1,(255,255,255))
        self.consoleScreen.blit(label, (self.fontHeight*0.25, self.consoleScreen.get_height()-self.fontHeight*2))
