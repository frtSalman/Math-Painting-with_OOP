from canvas import Canvas
from rectangle import Rectangle
from square import Square

cnv_width = int(input('Enter canvas width: '))
cnv_height = int(input('Enter canvas height: '))
cnv_color = input('Enter canvas color: ')
if cnv_color == 'black':
    bg = [0, 0, 0]
else:
    bg = [255, 255, 255]
cnv = Canvas(cnv_width, cnv_height, bg)
cnv.make()


while True:
    shape = input('What do you like to draw? Enter quit to quit: ')
    if shape == 'r':
        x = int(input('Enter x of rec: '))
        y = int(input('Enter y of rec: '))
        R = int(input('Enter R: '))
        G = int(input('Enter G: '))
        B = int(input('Enter B: '))
        width = int(input('Enter width: '))
        height = int(input('Enter height: '))
        rec = Rectangle(x, y, [R, G, B], width, height)
        rec.draw(cnv)
        continue
    elif shape == 's':
        x = int(input('Enter x of rec: '))
        y = int(input('Enter y of rec: '))
        R = int(input('Enter R: '))
        G = int(input('Enter G: '))
        B = int(input('Enter B: '))
        side = int(input('Enter side: '))
        sqr = Square(x, y, [R, G, B], side)
        sqr.draw(cnv)
        continue
    else:
        break
