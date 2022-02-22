import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("white")
t.color("green")
t.pensize(2)
t.speed(0)
s =1

for i in range(300):
	t.forward(s)
	t.right(91)
	s+=1