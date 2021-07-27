# Import turtle module
import turtle
# Import random module
import random

# Ask the user to input the length of the first square
# Range is limited between [20,60]
side_square = turtle.numinput('Rotating Colorful Squares and Disks', 'Please enter the side length of the first square[20-60]', 40, minval = 20, maxval = 60)

# turtle title
turtle.title('Rotating Colorful Squares and Disks')

# Hide the turtle
turtle.hideturtle()
# Speed up the drawing process in turtle
turtle.speed(0)
# Set colormode to 255
turtle.colormode(255)

# Move to coordinate (-150,0) without drawing  
turtle.up()
turtle.goto(-150,0)

# Set the orientation of the turtle to 90 degree
turtle.setheading(90)

# Pull the pen down
turtle.down()

# Draw 72 squares and fill squares with random color
for square in range(72):
    turtle.fillcolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    turtle.begin_fill()
    for side in range(4):
        turtle.forward(side_square)
        turtle.left(90)
    turtle.end_fill()

# Turn right 5 degrees for every new square
    turtle.right(5)
# The sides length of the new square always increases by 2 from the sides length of previous square
    side_square += 2

# To make suitable radius of circles or disks
side_square /= 2

# Set the orientation of the turtle to 0 degree
turtle.setheading(0)

# Move to cordinate (250,0) without drawing line
turtle.up()
turtle.goto(250,0)

# Pull the pen down
turtle.down()

# Draw 36 disks and fill 36 disks with random color
for side in range(36):
    turtle.fillcolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))   
    turtle.begin_fill()
    turtle.circle(side_square)
    turtle.end_fill()

# Turn left 10 degrees for every new disk
    turtle.left(10)
# The radius length of the new disk always decreases by 2 from the radius length of previous disk
    side_square -= 2

# Move to cordinate (0, -275) without drawing
turtle.up()
turtle.goto(0,-275)

# Write 'There are 72 Squares and 36 Disks' with blue color
turtle.pencolor('blue')
turtle.down()
turtle.write('There are 72 Squares and 36 Disks', align='center', font=('Arial', '12', 'bold'))



turtle.mainloop()
'''
Starts event loop - calling Tkinter’s mainloop function.
Must be the last statement in a turtle graphics program
for interactive use of turtle graphics
'''
