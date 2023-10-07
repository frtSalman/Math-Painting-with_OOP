from PIL import Image


class Rectangle:

    def __init__(self, x, y, color, width, height):
        self.y = y
        self.x = x
        self.color = color
        self.height = height
        self.width = width

    def draw(self, canvas):

        data = canvas.data
        data[self.x:self.x + self.height, self.y:self.y + self.width] = self.color
        img = Image.fromarray(data, 'RGB')
        img.save('canvas.png')
