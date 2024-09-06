from canvas import Canvas
from rectangle import Rectangle, Square
from render_image import RenderImage

def get_dimension(dimension, drawable):
    while True:
        try:
            value = int(input(f"Enter {dimension} of the {drawable}: "))
            if value <= 0:
                print(f"{dimension.capitalize()} must be a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def get_color():
    while True:
        try:
            red = int(input("How much red should the color have? "))
            green = int(input("How much green should the color have? "))
            blue = int(input("How much blue should the color have? "))

            if not all(0 <= c <= 255 for c in (red, green, blue)):
                raise ValueError("Each color component must be between 0 and 255.")

            return (red, green, blue)
        except ValueError as e:
            print(f"Invalid input: {e}")

def get_canvas_colour():
    valid_colours = {"black", "white"}
    while True:
        colour = input("Enter canvas colour (black or white): ").strip().lower()
        if colour in valid_colours:
            return colour
        else:
            print(f"Invalid colour. Only 'black' and 'white' are allowed. Got: {colour}")

def main():
    canvas_width = get_dimension("width", "canvas")
    canvas_height = get_dimension("height", "canvas")
    canvas_colour = get_canvas_colour()
    canvas = Canvas(canvas_width, canvas_height, canvas_colour)

    running = True

    while running:
        shape_to_draw = input("What shape would you like to draw (square or rectangle)? Enter 'quit' to exit: ").strip().lower()

        if shape_to_draw == "quit":
            running = False

        elif shape_to_draw == 'square':
            square_x = get_dimension("x", "square")
            square_y = get_dimension("y", "square")
            square_width = get_dimension("width", "square")
            square_color = get_color()
            square = Square(square_x, square_y, square_width, square_color)
            square.draw(canvas)

        elif shape_to_draw == 'rectangle':
            rectangle_x = get_dimension("x", "rectangle")
            rectangle_y = get_dimension("y", "rectangle")
            rectangle_width = get_dimension("width", "rectangle")
            rectangle_height = get_dimension("height", "rectangle")
            rectangle_color = get_color()
            rectangle = Rectangle(rectangle_x, rectangle_y, rectangle_width, rectangle_height, rectangle_color)
            rectangle.draw(canvas)

        else:
            print("Invalid shape. Please enter 'square', 'rectangle', or 'quit'.")

    filename = input("Enter filename for the image: ").strip()
    canvas.make(filename)
    render_image = RenderImage(filename)
    render_image.render_image()

if __name__ == "__main__":
    main()
