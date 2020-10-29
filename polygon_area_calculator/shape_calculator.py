
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, number):
        self.width = number

    def set_height(self, number):
        self.height = number

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        else:
            return ("*" * self.width + '\n') * self.height

    def get_amount_inside(self, new_object):
        w_inside = self.width // new_object.width
        h_inside = self.height // new_object.height
        return int(w_inside * h_inside)
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})" # return string object


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side) # get values from parent init function(from rectangle class)

    def set_side(self, number):
        super().set_width(number) # access methods from rectangle class
        super().set_height(number)

    def __str__(self):
        return f"Square(side={self.width})" # return string object
