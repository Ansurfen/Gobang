from pygame import font


class Button:
    def __init__(self, text, color, x=None, y=None):
        self.font = font.SysFont('SimHei', 30)
        self.surface = self.font.render(text, True, color)
        self.WIDTH = self.surface.get_width()
        self.HEIGHT = self.surface.get_height()
        self.loc = (x, y)

    def display(self, window):
        window.blit(self.surface, self.loc)

    def click(self, pos):
        x_match = pos[0] > self.loc[0] and pos[0] < self.loc[0] + self.WIDTH
        y_match = pos[1] > self.loc[1] and pos[1] < self.loc[1] + self.HEIGHT

        if x_match and y_match:
            return True
        else:
            return False
