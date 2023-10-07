from PIL import Image


class Square:

    def __init__(self, x, y, color, side):
        self.side = side
        self.y = y
        self.x = x
        self.color = color

    def draw(self, canvas):

        data = canvas.data
        data[self.x:self.x + self.side, self.y:self.y + self.side] = self.color
        img = Image.fromarray(data, 'RGB')
        img.save('canvas.png')
