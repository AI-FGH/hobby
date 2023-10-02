import turtle


# Set up the turtle screen

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Islamic Republic of Iran National Flag")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)

# Function to draw a 3 colored filled rectangle
def draw_filled_rectangle(color, width, height):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Draw green rectangle in the middle
t.penup()
t.goto(-100, 50)
t.pendown()
draw_filled_rectangle("green", 1000, 200)

# Draw white rectangle overlapping with the green one
t.penup()
t.goto(-100, -150)
t.pendown()
draw_filled_rectangle("white", 1000, 200)
# Draw red rectangle below the white one
t.penup()
t.goto(-100, -350)
t.pendown()
draw_filled_rectangle("red", 1000, 200)
# Draw little squres

t.penup()
t.goto(-100, -145)
t.pendown()
def draw_square(size,color):
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()
square_size = 4
distance_between_squares = 41.25
for _ in range(23):
    draw_square(square_size,'red')  # Draw a square
    t.penup()
    t.forward(square_size + distance_between_squares)  # Move to the next position
    t.pendown()

t.penup()
t.goto(-100,50)
t.pendown()
for _ in range(23):
    draw_square(square_size,'green')  # Draw a square
    t.penup()
    t.forward(square_size + distance_between_squares)  # Move to the next position
    t.pendown()


######################################################################################
# Draw 11 black rectangles with a distance of 10 between them for allaho akbar
t.penup()
t.goto(-95, 70)
t.pendown()
def draw_filled_rectangle_w(width, height):
    t.color("white")
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
rectangle_width = 57.4
rectangle_height = 2
distance_between_rectangles = 33.6
for _ in range(11):
    draw_filled_rectangle_w(rectangle_width, rectangle_height)  # Draw a black rectangle
    t.penup()
    t.forward(rectangle_width + distance_between_rectangles)  # Move to the next position
    t.pendown()

t.penup()
t.goto(-95, 65)
t.pendown()
rectangle_width = 19
rectangle_height = 2
distance_between_rectangles = 72
for _ in range(11):
    draw_filled_rectangle_w(rectangle_width, rectangle_height)  # Draw a black rectangle
    t.penup()
    t.forward(rectangle_width + distance_between_rectangles)  # Move to the next position
    t.pendown()


t.penup()
t.goto(-95, 56)
t.pendown()

def draw_filled_rectangle_q(color, width, height):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
# Draw 3 vertical black rectangles with no space between them
rectangle_width = 2
rectangle_height = 10

for _ in range(11):
     # Draw a black rectangle
    draw_filled_rectangle_q("white", rectangle_width, rectangle_height)
    t.penup()
    t.forward(rectangle_width + 89)  # Move to the next position
    t.pendown()


t.penup()
t.goto(-78, 56)
t.pendown()

# Draw 3 vertical black rectangles with no space between them
rectangle_width = 2
rectangle_height = 10

for _ in range(11):
     # Draw a black rectangle
    draw_filled_rectangle_q("white", rectangle_width, rectangle_height)
    t.penup()
    t.forward(rectangle_width + 89)  # Move to the next position
    t.pendown()



t.penup()
t.goto(-60, 56)
t.pendown()

for _ in range(11):
     # Draw a black rectangle
    draw_filled_rectangle_q("white", rectangle_width, rectangle_height)
    t.penup()
    t.forward(rectangle_width + 88.8)  # Move to the next position
    t.pendown()

t.penup()
t.goto(-77, 55)
t.pendown()
rectangle_width = 18
rectangle_height = 2
distance_between_rectangles = 72.9
for _ in range(11):
    draw_filled_rectangle_w(rectangle_width, rectangle_height)  # Draw a black rectangle
    t.penup()
    t.forward(rectangle_width + distance_between_rectangles)  # Move to the next position
    t.pendown()



t.penup()
t.goto(-68, 65)
t.pendown()

# Draw 3 vertical black rectangles with no space between them
rectangle_width = 8.7
rectangle_height = 2

for _ in range(11):
     # Draw a black rectangle
    draw_filled_rectangle_q("white", rectangle_width, rectangle_height)
    t.penup()
    t.forward(rectangle_width + 82)  # Move to the next position
    t.pendown()


x = -30
for _ in range(11):
    t.penup()
    t.goto(x, 55)
    t.pendown()
    rectangle_width = 2
    rectangle_height = 18
    for _ in range(3):
        draw_filled_rectangle("white", rectangle_width, rectangle_height)  # Draw a black rectangle
        t.penup()
        t.forward(rectangle_width + 7)  # Move to the next position
        t.pendown()
    horizontal_rectangle_width = 18
    horizontal_rectangle_height = 2
    t.penup()
    t.goto(x, 55)
    t.pendown()
    draw_filled_rectangle("white", horizontal_rectangle_width, horizontal_rectangle_height)
    x = x + 90.5



t.penup()
t.goto(-50, 65)
t.pendown()

#
rectangle_width = 18.1
rectangle_height = 2

for _ in range(11):
     # Draw a black rectangle
    draw_filled_rectangle_q("white", rectangle_width, rectangle_height)
    t.penup()
    t.forward(rectangle_width + 72.7)  # Move to the next position
    t.pendown()



t.penup()
t.goto(-50, 55)
t.pendown()
rectangle_width = 2
rectangle_height = 10
distance_between_rectangles = 88.8
for _ in range(11):
    draw_filled_rectangle_w(rectangle_width, rectangle_height)  # Draw a black rectangle
    t.penup()
    t.forward(rectangle_width + distance_between_rectangles)  # Move to the next position
    t.pendown()


t.penup()
t.goto(-50, 55)
t.pendown()

# Draw 3 vertical black rectangles with no space between them
rectangle_width = 12
rectangle_height = 2
for _ in range(11):
     # Draw a black rectangle
    draw_filled_rectangle_q("white", rectangle_width, rectangle_height)
    t.penup()
    t.forward(rectangle_width + 79)  # Move to the next position
    t.pendown()

# Draw point of akbar

square_size = 2
distance_between_squares = 88.95
t.penup()
t.goto(-87,60)
t.pendown()
for _ in range(11):
    draw_square(square_size,'white')  # Draw a square
    t.penup()
    t.forward(square_size + distance_between_squares)  # Move to the next position
    t.pendown()


######################################################################################
# Draw 11 black rectangles with a distance of 10 between them for allaho akbar
t.penup()
t.goto(-95, -155)
t.pendown()
def draw_filled_rectangle_w(width, height):
    t.color("white")
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
rectangle_width = 57.4
rectangle_height = 2
distance_between_rectangles = 33.6
for _ in range(11):
    draw_filled_rectangle_w(rectangle_width, rectangle_height)  # Draw a black rectangle
    t.penup()
    t.forward(rectangle_width + distance_between_rectangles)  # Move to the next position
    t.pendown()

t.penup()
t.goto(-95, -160)
t.pendown()
rectangle_width = 19
rectangle_height = 2
distance_between_rectangles = 72
for _ in range(11):
    draw_filled_rectangle_w(rectangle_width, rectangle_height)  # Draw a black rectangle
    t.penup()
    t.forward(rectangle_width + distance_between_rectangles)  # Move to the next position
    t.pendown()


t.penup()
t.goto(-95, -171)
t.pendown()

def draw_filled_rectangle_q(color, width, height):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
# Draw 3 vertical black rectangles with no space between them
rectangle_width = 2
rectangle_height = 10

for _ in range(11):
     # Draw a black rectangle
    draw_filled_rectangle_q("white", rectangle_width, rectangle_height)
    t.penup()
    t.forward(rectangle_width + 89)  # Move to the next position
    t.pendown()



t.penup()
t.goto(-78, -171)
t.pendown()

# Draw 3 vertical black rectangles with no space between them
rectangle_width = 2
rectangle_height = 10

for _ in range(11):
     # Draw a black rectangle
    draw_filled_rectangle_q("white", rectangle_width, rectangle_height)
    t.penup()
    t.forward(rectangle_width + 89)  # Move to the next position
    t.pendown()



t.penup()
t.goto(-60, -171)
t.pendown()

for _ in range(11):
     # Draw a black rectangle
    draw_filled_rectangle_q("white", rectangle_width, rectangle_height)
    t.penup()
    t.forward(rectangle_width + 88.8)  # Move to the next position
    t.pendown()

t.penup()
t.goto(-77, -171)
t.pendown()
rectangle_width = 18
rectangle_height = 2
distance_between_rectangles = 72.9
for _ in range(11):
    draw_filled_rectangle_w(rectangle_width, rectangle_height)  # Draw a black rectangle
    t.penup()
    t.forward(rectangle_width + distance_between_rectangles)  # Move to the next position
    t.pendown()



t.penup()
t.goto(-67, -160)
t.pendown()

# Draw 3 vertical black rectangles with no space between them
rectangle_width = 8.83
rectangle_height = 2

for _ in range(11):
     # Draw a black rectangle
    draw_filled_rectangle_q("white", rectangle_width, rectangle_height)
    t.penup()
    t.forward(rectangle_width + 82)  # Move to the next position
    t.pendown()


x = -30
for _ in range(11):
    t.penup()
    t.goto(x, -171)
    t.pendown()
    rectangle_width = 2
    rectangle_height = 18
    for _ in range(3):
        draw_filled_rectangle("white", rectangle_width, rectangle_height)  # Draw a black rectangle
        t.penup()
        t.forward(rectangle_width + 7)  # Move to the next position
        t.pendown()
    horizontal_rectangle_width = 18
    horizontal_rectangle_height = 2
    t.penup()
    t.goto(x, -171)
    t.pendown()
    draw_filled_rectangle("white", horizontal_rectangle_width, horizontal_rectangle_height)
    x = x + 90.5



t.penup()
t.goto(-50,-160)
t.pendown()

#
rectangle_width = 18.1
rectangle_height = 2

for _ in range(11):
     # Draw a black rectangle
    draw_filled_rectangle_q("white", rectangle_width, rectangle_height)
    t.penup()
    t.forward(rectangle_width + 72.7)  # Move to the next position
    t.pendown()



t.penup()
t.goto(-50, -171)
t.pendown()
rectangle_width = 2
rectangle_height = 10
distance_between_rectangles = 88.8
for _ in range(11):
    draw_filled_rectangle_w(rectangle_width, rectangle_height)  # Draw a black rectangle
    t.penup()
    t.forward(rectangle_width + distance_between_rectangles)  # Move to the next position
    t.pendown()


t.penup()
t.goto(-50, -171)
t.pendown()

# Draw 3 vertical black rectangles with no space between them
rectangle_width = 12
rectangle_height = 2
for _ in range(11):
     # Draw a black rectangle
    draw_filled_rectangle_q("white", rectangle_width, rectangle_height)
    t.penup()
    t.forward(rectangle_width + 79)  # Move to the next position
    t.pendown()

# Draw point of akbar

square_size = 2
distance_between_squares = 88.95
t.penup()
t.goto(-87,-165)
t.pendown()
for _ in range(11):
    draw_square(square_size,'white')  # Draw a square
    t.penup()
    t.forward(square_size + distance_between_squares)  # Move to the next position
    t.pendown()



#######################################################################################

def draw_filled_circle(color, radius):
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw red luna in the middle of the page
moon_radius = 40 # Radius of the moon
shadow_radius = 60 # Radius of the moon's shadow
moon_color = "red"
shadow_color = "white"

# Draw the moon
t.penup()
t.goto(370, -85 )  # Move to the starting position
t.pendown()
draw_filled_circle(moon_color, moon_radius)
t.penup()
t.goto(430, -85 )  # Move to the starting position
t.pendown()
draw_filled_circle(moon_color, moon_radius)
# Draw the moon's shadow
t.penup()
t.goto(400, -105 )  # Move to the starting position of the shadow
t.pendown()
draw_filled_circle(shadow_color, shadow_radius)

#++++++++++++++++++++++++++++++++++++++++++++
def draw_filled_half(color, radius,d):
    t.color(color)
    t.begin_fill()
    t.circle(radius,d)
    t.end_fill()
moon_radius =60# Radius of the moon
shadow_radius = 70 # Radius of the moon's shadow
moon_color = "red"
shadow_color = "white"

# Draw the moon
t.penup()
t.goto(409, -108)  # Move to the starting position
t.pendown()
draw_filled_half(moon_color, moon_radius,-130)
t.penup()
t.goto(374.3, 0)  # Move to the starting position of the shadow
t.pendown()
draw_filled_half(shadow_color, shadow_radius,130)
#______________________________________________________


# Draw the moon
t.penup()
t.goto(392, -110)  # Move to the starting position
t.pendown()
draw_filled_half(moon_color, moon_radius, 130)
moon_radius =63# Radius of the moon
shadow_radius = 70 # Radius of the moon's shadow
t.penup()
t.goto(427, 0)  # Move to the starting position of the shadow
t.pendown()
draw_filled_half(shadow_color, shadow_radius, -130)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

###################################################
def draw_curved_line(radius, angle, direction):
    t.color('red')
    t.circle(radius, angle * direction)
t.pensize(4.5)
t.penup()
t.goto(422, -115)
t.pendown()

# Draw the custom curved line
radius = 70  # Radius of the curve
angle = 120  # Angle of the curve (180 degrees for a semi-circle)
direction = -1   # 1 for clockwise, -1 for counterclockwise
draw_curved_line(radius, angle, direction)
t.penup()
t.setheading(0)  # Set turtle's orientation to the right
t.pendown()

t.pensize(4)
t.penup()
t.goto(380, -115)
t.pendown()
# Draw the custom curved line
radius = 70 # Radius of the curve
angle = 120 # Angle of the curve (180 degrees for a semi-circle)
direction = 1  # 1 for clockwise, -1 for counterclockwise
draw_curved_line(radius, angle, direction)
#@@@
def draw_red_triangle_upside(size):
    t.color("red")
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.right(120)
    t.end_fill()

# Set pen size and position
t.pensize(2)
t.penup()
t.goto(402, -122)  # Set starting position for the triangle
t.pendown()

# Draw the upside-down red triangle
triangle_size = 12
draw_red_triangle_upside(triangle_size)
t.penup()
t.setheading(0)  # Set turtle's orientation to the right
t.pendown()
#@@
color = 'red'
t.penup()
t.goto(400, -110)  # Set starting position for the triangle
t.pendown()
width = 5
height = 98
draw_filled_rectangle_q(color, width, height)

def draw_red_triangle(size):
    t.color("red")
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()
t.penup()
t.setheading(0)  # Set turtle's orientation to the right
t.pendown()
# Set pen size and position
t.pensize(2)
t.penup()
t.goto(399, -13)  # Set starting position for the triangle
t.pendown()
trian= 6
draw_red_triangle(trian)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

t.penup()
t.goto(392, -5)
t.pendown()


color = "red"
shadow_color = "white"

# Draw the moon

draw_filled_circle(color, 18)
t.penup()
t.goto(408, -5)
t.pendown()
draw_filled_circle(color, 18)


t.penup()
t.goto(390, 0)
t.pendown()

draw_filled_circle(shadow_color, 20)
t.penup()
t.goto(410, 0)
t.pendown()
draw_filled_circle(shadow_color, 20)

#***********************************************************************************************
text = "We are . . . "

t.penup()
t.goto(-900, 100)
t.pendown()
t.color('black')  # Set font color
t.write(text, align="left", font=("time ", 50, "normal"))

text = "Nation of IMAM HOSSAIN"
t.penup()
t.goto(-900, -100)
t.pendown()
t.color('black')  # Set font color
t.write(text, align="left", font=("time ", 50, "normal"))


# Write the text aligned to the left

# Close the turtle graphics window when clicked
screen.exitonclick()
