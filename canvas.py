import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, width, height, color):
        self.color = color
        self.height = height
        self.width = width
        self.data = np.zeros(shape=(self.height, self.width, 3), dtype=np.uint8)

    def make(self):

        self.data[:] = self.color

        img = Image.fromarray(self.data, 'RGB')

        img.save('canvas.png')
