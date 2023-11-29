import turtle, random, time
from random import randint

screen = turtle.Screen()
screen.title("Turtle Oyunu")
screen.bgcolor("white")

t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.speed(0)
t.penup()

oyun_suresi = 20
tiklama_sayisi = 0
def geri_sayim():
    global tiklama_sayisi
    for i in range(oyun_suresi, 0, -1):
        x = randint(-300, 300)
        y = randint(-300, 300)
        t.goto(x, y)


        t.write("Zaman: {} Saniye - Tıklanma: {}".format(i, tiklama_sayisi), align="center", font=("Arial", 16, "normal"))
        screen.update()  #
        time.sleep(1)
        t.clear()

    oyunu_bitir()
def oyunu_bitir():
    t.hideturtle()
    t.goto(0, 0)
    t.write("Oyun Bitti - Tıklanma: {}".format(tiklama_sayisi), align="center", font=("Arial", 20, "bold"))
    screen.update()

def tiklama(x, y):
    global tiklama_sayisi
    if t.distance(x, y) < 20:  
        tiklama_sayisi += 1

screen.onclick(tiklama)

screen.ontimer(geri_sayim, 0)

while True:
    aci = random.randint(0, 360)
    t.setheading(aci)
    t.forward(50)
    screen.update()
    time.sleep(0.5)