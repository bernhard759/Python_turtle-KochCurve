# Import
import turtle


# Function for drawing a curve
def koch_curve(t, order, size):
  if order == 0:
    t.forward(size)
  else:
    # Recursive call for each angle
    for angle in [60, -120, 60, 0]:
      koch_curve(t, order - 1, size / 3)
      t.left(angle)


# Drawer func
def draw_koch_curve(order, size):
  window = turtle.Screen()
  window.bgcolor("white")
  window.title("Koch Curve Fractal")

  fractal_turtle = turtle.Turtle()
  fractal_turtle.color("blue")
  fractal_turtle.penup()
  fractal_turtle.goto(-size / 2, size / 4)
  fractal_turtle.pendown()
  fractal_turtle.speed(0)

  # Start drawing here
  for _ in range(3):
    koch_curve(fractal_turtle, order, size)
    fractal_turtle.right(120)

  window.mainloop()


# Adjust order and size to change the complexity and size of the fractal
order = 4
size = 300

# Start the turtle
draw_koch_curve(order, size)
