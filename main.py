from turtle import *
from random import randint

speed(10)
penup()
goto(-140, 140)  # déplace la tortue à l'endroit où on veut commencer

for etape in range(14):
    write(etape, align='center')
    right(90)  # tourne à droite de 90°
    forward(10)  # On avance de 10 pixels
    pendown()  # On baisse le crayon
    forward(150)  # On avance de 150 pixels
    penup()  # On lève le crayon
    backward(160)  # 160 pixels vers l'arrière
    left(90)  # On tourne à gauche de 90°
    forward(20)  # On avance de 20 pixels

ada = Turtle()  # On crée une nouvelle tortue
ada.color('red')  # On lui donne une couleur
ada.shape('turtle')  # On lui donne une forme

ada.penup()  # On lève le crayon
ada.goto(-160, 100)  # On la place à l'endroit où on veut commencer
ada.pendown()  # On baisse le crayon

bob = Turtle()  # On crée une nouvelle tortue
bob.color('blue')  # On lui donne une couleur
bob.shape('turtle')  # On lui donne une forme

bob.penup()  # On lève le crayon
bob.goto(-160, 70)  # On la place à l'endroit où on veut commencer
bob.pendown()  # On baisse le crayon

for tourner in range(100):
    ada.forward(randint(1, 5))  # On avance de 1 à 5 pixels
    bob.forward(randint(1, 5))  # On avance de 1 à 5 pixels


# vérifiez quel tortue a gagné
if ada.xcor() > bob.xcor():
    print("Ada a gagné !")
elif ada.xcor() < bob.xcor():
    print("Bob a gagné !")
else:
    print("Egalité !")

# On ferme la fenêtre s'il y a un clique gauche
exitonclick()