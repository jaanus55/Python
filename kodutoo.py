import turtle

def draw_plus_outline(x, y, size):
  
    turtle.penup()
    turtle.goto(x - size, y + size // 2)
    turtle.pendown()
    
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.left(90)
      
    turtle.penup()

def main():
    turtle.speed(0)
    size = 30
    positions = [(0, 0), (size, - size * 2), (size * 2, size), (size * 3, - size)]
    
    for pos in positions:
        draw_plus_outline(pos[0], pos[1], size)
    
    turtle.hideturtle()
    turtle.done()

main()