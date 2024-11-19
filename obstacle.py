from kivy.uix.widget import Widget

class Obstacle(Widget):
    def __init__(self, x, y, height, width):
        super(Obstacle, self).__init__()
        self.x = x
        self.y = y
        self.height = height
        self.width = width



