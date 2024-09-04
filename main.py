from canvas import Canvas
from rectangle import Rectangle, Square
from save_image import SaveImage

canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))
canvas_colour = input("Enter canvas colour (black or white): ")
canvas = Canvas(canvas_width, canvas_height, canvas_colour)
canvas = canvas.draw()

running = True

while running:
    shape_to_draw = input("What shape would you like to draw (square or rectangle)? Enter quit to exit when you are done. :) ")
    if shape_to_draw == "quit":
        filename = input("Enter filename for the image: ")
        save_image = SaveImage(filename)
        save_image.save(pillow_image)
        running = False
        
        continue
    
    if shape_to_draw == 'square':
        square_x = int(input("Enter x of the square: "))
        square_y = int(input("Enter y of the square: "))
        square_width = int(input("Enter width of the square: "))
        square_red = int(input("How much red should the square have? "))
        square_green = int(input("How much green should the square have? "))
        square_blue = int(input("How much blue should the square have? "))
        square = Square(square_x, square_y, square_width, red=255, green=155, blue=0)
        canvas, pillow_image = square.draw(canvas)
        
    else:
        rectangle_x = int(input("Enter x of the rectangle: "))
        rectangle_y = int(input("Enter y of the rectangle: "))
        rectangle_width = int(input("Enter width of the rectangle: "))
        rectangle_height = int(input("Enter height of the rectangle: "))
        rectangle_red = int(input("How much red should the rectangle have? "))
        rectangle_green = int(input("How much green should the rectangle have? "))
        rectangle_blue = int(input("How much blue should the rectangle have? "))
        rectangle = Rectangle(rectangle_x, rectangle_y, rectangle_width, rectangle_height, rectangle_red, rectangle_green, rectangle_blue)
        canvas, pillow_image = rectangle.draw(canvas)

