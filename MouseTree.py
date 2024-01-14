import turtle

def fractal_tree(turtle, branch_length, angle):
    if branch_length < 5:  # Base case: stop recursion when branch length is small
        return
    else:
        # Draw the main branch
        turtle.forward(branch_length)

        # Right branch (recursion)
        turtle.right(angle)
        fractal_tree(turtle, branch_length - 15, angle)

        # Left branch (recursion)
        turtle.left(2 * angle)
        fractal_tree(turtle, branch_length - 15, angle)

        # Back to the original position
        turtle.right(angle)
        turtle.backward(branch_length)

def update_angle(x, y):
    # Calculate the angle based on the mouse x-coordinate
    new_angle = (x - screen_width / 2) / 10  # Adjust the factor to control sensitivity
    tree_turtle.setheading(new_angle)

def main():
    global screen_width
    screen = turtle.Screen()
    screen.bgcolor("white")
    tree_turtle = turtle.Turtle()
    tree_turtle.color("green")
    tree_turtle.speed(0)  # Set the drawing speed (0 is the fastest)

    # Position the turtle
    tree_turtle.left(90)
    tree_turtle.up()
    tree_turtle.backward(100)
    tree_turtle.down()

    # Calculate the screen width for angle adjustment
    screen_width = screen.window_width()

    # Register the update_angle function to be called when the mouse is moved
    screen.onscreenclick(update_angle)

    # Call the function to draw the fractal tree
    fractal_tree(tree_turtle, 100, 20)

    screen.mainloop()

if __name__ == "__main__":
    main()
