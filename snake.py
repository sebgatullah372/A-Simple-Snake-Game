import turtle
import time
import random

score = 0 
highest_score = 0

#screen
window= turtle.Screen()
window.title("Snake Game")
window.bgcolor("Green")
window.setup(width=600, height= 600)
window.tracer(0)

#snake
snake= turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("blue")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"


#food
food= turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


grow_snake= []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

#Function

def up():
	if snake.direction != "down":
		snake.direction= "up"
def down():
	if snake.direction != "up":
		snake.direction= "down"
def left():
	if snake.direction != "right":
		snake.direction= "left"
def right():
	if snake.direction != "left":
		snake.direction= "right"	

def move():
	if snake.direction == "up":
		y= snake.ycor()
		snake.sety(y+20)
	if snake.direction == "down":
		y= snake.ycor()
		snake.sety(y-20)
	if snake.direction == "left":
		x= snake.xcor()
		snake.setx(x-20)	
	if snake.direction == "right":
		x= snake.xcor()
		snake.setx(x+20)
		
		  
#Keypress
window.listen()
window.onkeypress(up,"w")
window.onkeypress(down,"s")
window.onkeypress(left,"a")
window.onkeypress(right,"d")



#Main Loop
while True:
	window.update()



	#Collision with the border

	if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290:
		time.sleep(1)
		snake.goto(0,0)
		snake.direction= "stop"
        #Hide Segment
		for grows in grow_snake:
			grows.goto(1000,1000)
		#Clear Segment
		grow_snake.clear()

		#reset
		score= 0
		
		pen.clear()

		pen.write("Score: {}  High Score: {} ".format(score,highest_score), align="center", font=("Courier", 24, "normal"))
		




	#Eat Food & Grow

	if snake.distance(food)<20:
		x= random.randint(-290,290)
		y= random.randint(-290,290)
		food.goto(x,y)
		
		grow= turtle.Turtle()
		grow.speed(0)
		grow.shape("square")
		grow.color("yellow")
		grow.penup()
		grow_snake.append(grow)

		score+=1

		if score>highest_score:
			highest_score= score
		pen.clear()

		pen.write("Score: {}  High Score: {} ".format(score,highest_score), align="center", font=("Courier", 24, "normal"))


    #Reverse
	for index in range(len(grow_snake)-1 ,0 ,-1):
		x= grow_snake[index-1].xcor()
		y= grow_snake[index-1].ycor()
		grow_snake[index].goto(x,y)
	#Move Segment to head	
	if len(grow_snake)>0:
		x= snake.xcor()
		y= snake.ycor()
		grow_snake[0].goto(x,y)


	move()

	#Check head hitting own body
	for grows in grow_snake:
		if grows.distance(snake)<20:
			time.sleep(1)
			snake.goto(0,0)
			snake.direction= "stop"
			for grows in grow_snake:
				grows.goto(1000,1000)
			grow_snake.clear()






	time.sleep(0.1)



window.mainloop()
        
