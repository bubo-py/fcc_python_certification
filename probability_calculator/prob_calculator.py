import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs): # unpack all given values (** - unpacking operator)
        self.kwargs = kwargs
        self.contents = []
        for key in self.kwargs.keys(): # get actual contents i.e. given balls
            for k in range(self.kwargs[key]):
                self.contents.append(key)

    def draw(self, number):
        # if you don't have enough balls to draw, return contents without doing anything
        if number >= len(self.contents):
            return self.contents

        else:
            chose = []
            for n in range(number):
                indexing = random.randrange(len(self.contents)) # choose random number from contents range
                chose_ball = self.contents[indexing] # chose ball variable
                chose.append(chose_ball) # adding to list of chose balls
                
                self.contents = self.contents[0:indexing] + self.contents[indexing + 1:] # updating contents list
                
            return chose

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    c = 0
    for n in range(num_experiments):
        n_hat = copy.copy(hat) # copy created hat class with given arguments
        n_draw = n_hat.draw(num_balls_drawn) # draw balls using class' function
        bleh = True
        for key in expected_balls.keys(): # looping through dictionary keys
            if n_draw.count(key) < expected_balls[key]:
                bleh = False
                break # end the loop if values are incorrect
        if bleh:
            c += 1 # if everything is correct, increment the value

        probability = c / num_experiments
    return probability
