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
        
        if number >= len(self.contents):
            return self.contents

        else:
            chose = []
            for n in range(number):
                indexing = random.randrange(len(self.contents))
                chose_ball = self.contents[indexing]
                chose.append(chose_ball)
                
                self.contents = self.contents[0:indexing] + self.contents[indexing + 1:]
                
            return chose

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    c = 0
    for n in range(num_experiments):
        n_hat = copy.copy(hat)
        n_draw = n_hat.draw(num_balls_drawn)
        bleh = True
        for key in expected_balls.keys():
            if n_draw.count(key) < expected_balls[key]:
                bleh = False
                break
        if bleh:
            c += 1

        probability = c / num_experiments
    return probability
