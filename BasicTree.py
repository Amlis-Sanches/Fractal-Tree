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

        # Back to original position
        turtle.right(angle)
        turtle.backward(branch_length)

def main():
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

    # Call the function to draw the fractal tree
    fractal_tree(tree_turtle, 100, 20)

    screen.exitonclick()

if __name__ == "__main__":
    main()
