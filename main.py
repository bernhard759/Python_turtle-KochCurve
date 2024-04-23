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
def draw_koch_curve(order, size, x, y, color):
  fractal_turtle = turtle.Turtle()
  fractal_turtle.penup()
  fractal_turtle.goto(x, y)
  fractal_turtle.pendown()
  fractal_turtle.speed(0)
  fractal_turtle.begin_fill()
  fractal_turtle.fillcolor(color)

  for _ in range(3):
    koch_curve(fractal_turtle, order, size)
    fractal_turtle.right(120)

  fractal_turtle.end_fill()


def draw_grid():
  window = turtle.Screen()
  window.bgcolor("white")
  window.title("Koch Curve Fractal Grid")
  window_width, window_height = 400, 400
  window.setup(width=window_width, height=window_height)

  cell_size = 200
  cell_offset = cell_size / 2

  colors = ["brown", "darkcyan", "AliceBlue", "goldenrod"]

  for i in range(2):
    for j in range(2):
      order = 1 + i * 2 + j
      x = j * cell_size - cell_offset
      y = i * cell_size - cell_offset
      print("Drawing with order", order, "at", x, y)
      draw_koch_curve(order, 150, x, y, colors[i * 2 + j])

  window.mainloop()


draw_grid()
