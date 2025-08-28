import turtle

# Setup
t = turtle.Turtle()
t.speed(8)
screen = turtle.Screen()
screen.bgcolor("white")
turtle.title("Lord Krishna guiding Arjuna")

def circle(x, y, r, color):
    """Draw a filled circle at (x, y)"""
    t.penup()
    t.goto(x, y - r)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

# --- Chariot Base ---
t.pensize(3)
t.penup()
t.goto(-200, -100)
t.pendown()
t.fillcolor("gold")
t.begin_fill()
for _ in range(2):
    t.forward(400)
    t.left(90)
    t.forward(100)
    t.left(90)
t.end_fill()

# Wheels
circle(-150, -100, 40, "black")
circle(150, -100, 40, "black")

# --- Krishna ---
circle(-50, 50, 40, "skyblue")   # Krishna head
circle(-70, 100, 10, "green")    # Peacock feather
circle(-35, 60, 5, "white")      # Eye left
circle(-15, 60, 5, "white")      # Eye right

# Krishna body
t.pensize(15)
t.pencolor("skyblue")
t.penup()
t.goto(-50, 10)
t.pendown()
t.goto(-50, -50)

# Krishna hand (showing guidance)
t.goto(-10, -20)

# --- Arjuna ---
circle(70, 50, 40, "#f7cba4")    # Arjuna head
circle(55, 60, 5, "black")       # Eye left
circle(85, 60, 5, "black")       # Eye right

# Arjuna body
t.pensize(15)
t.pencolor("#f7cba4")
t.penup()
t.goto(70, 10)
t.pendown()
t.goto(70, -50)

# Arjuna’s bow
t.pensize(3)
t.pencolor("brown")
t.penup()
t.goto(120, 10)
t.pendown()
t.circle(60, 180)

# --- Horses (symbolic) ---
circle(-250, -20, 30, "gray")
circle(-320, -20, 30, "gray")
circle(-390, -20, 30, "gray")

# --- Title ---
t.penup()
t.goto(-200, 150)
t.pencolor("darkblue")
t.write("Lord Krishna guiding Arjuna", font=("Arial", 20, "bold"))

t.hideturtle()
turtle.done()
