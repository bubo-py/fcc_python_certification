import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = []
        for key in self.kwargs.keys():
            for k in range(self.kwargs[key]):
                self.contents.append(key)

    def draw(self, number):
        chose = []
        for x in range(number):
            drawing = random.choice(self.contents)
            chose.append(drawing)
            self.contents.pop(self.contents.index(drawing))
        return chose

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass
