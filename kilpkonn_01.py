#M.Metshein
#10.10.22
#Kilpkonna liikumise harjutamine
import turtle


#tekitan akna ja lisan muutujasse
aken = turtle.Screen()
aken.setup(300,300)
aken.title("Kilpkonna harjutus 01")

#konna loomine
konn1 = turtle.Turtle()
konn1.color("lime")
konn1.left(0)
konn1.forward(100)

konn2 = turtle.Turtle()
konn2.color("red")
konn2.left(45)
konn2.forward(100)

konn4 = turtle.Turtle()
konn4.color("orange")
konn4.left(90)
konn4.forward(100)

konn3 = turtle.Turtle()
konn3.color("blue")
konn3.left(135)
konn3.forward(100)


"""
konn1 = turtle.Turtle()
konn1.color("lime")
konn1.forward(100)
konn1.penup() #pliiats üles
konn1.left(180)
konn1.forward(100)
konn1.left(45)
konn1.pendown() #pliiats alla
konn1.color("red")
konn1.backward(100)
turtle.exitonclick()
"""