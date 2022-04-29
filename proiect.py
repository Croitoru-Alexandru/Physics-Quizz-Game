import turtle
import random

display = turtle.Screen()
display.setup(1920,1080)
display.bgpic("Backgorund.gif")
display.addshape("mar.gif")
display.addshape("einstein.gif")

mar = turtle.Turtle()
mar.shape("mar.gif")
mar.penup()
mar.goto(-520,5)

einstein = turtle.Turtle()
einstein.shape("einstein.gif")
einstein.penup()
einstein.goto(550, 5)


figura = turtle.Turtle()
figura.hideturtle()
figura.speed(0)
figura.color("white")
figura.penup()
figura.goto(550, 250)
figura.pendown()
figura.shape('turtle')

for i in range(20):
    figura.left(30)
    figura.forward(100)
    figura.left(5)
    figura.forward(10)
    figura.left(90)
    figura.forward(100)
    figura.left(60)

figura1 = turtle.Turtle()
figura1.hideturtle()
figura1.speed(0)
figura1.color("white")
figura1.penup()
figura1.goto(550, -350)
figura1.pendown()
figura1.shape('turtle')

for i in range(20):
    figura1.left(30)
    figura1.forward(100)
    figura1.left(5)
    figura1.forward(10)
    figura1.left(90)
    figura1.forward(100)
    figura1.left(60)

figura2 = turtle.Turtle()
figura2.hideturtle()
figura2.speed(0)
figura2.color("white")
figura2.penup()
figura2.goto(-550, -350)
figura2.pendown()
figura2.shape('turtle')

for i in range(20):
    figura2.left(30)
    figura2.forward(100)
    figura2.left(5)
    figura2.forward(10)
    figura2.left(90)
    figura2.forward(100)
    figura2.left(60)

figura3 = turtle.Turtle()
figura3.hideturtle()
figura3.speed(0)
figura3.color("white")
figura3.penup()
figura3.goto(-550, 250)
figura3.pendown()
figura3.shape('turtle')

for i in range(20):
    figura3.left(30)
    figura3.forward(100)
    figura3.left(5)
    figura3.forward(10)
    figura3.left(90)
    figura3.forward(100)
    figura3.left(60)

text = turtle.Turtle()
text.hideturtle()
text.color("#01FEED")
style = ('Courier', 30, 'italic')
text.penup()
text.goto(0, 300)
text.pendown()
text.write(f"Bine ai venit la jocul JOC!", move=True, align="center", font=style)
text.penup()

pix = turtle.Turtle()
pix.hideturtle()
pix.color('#3CFE01')
style1 = ('Courier', 15, 'italic')
pix.penup()
pix.goto(0, 100)
pix.pendown()

score = turtle.Turtle()
score.hideturtle()
score.color('#FEBB01')
style2 = ('Courier', 20, 'italic')
score.penup()
score.goto(0, 200)
score.pendown()
scor = 0
score.write(f"Score: {scor}", align='center', font=style2)

def intrebare1(x):
    while True:
        global scor
        intrebare = x
        if intrebare == 1:
            pix.write(f"1. Cate principii are mecanica clasica?", move=True, align='center', font=style1)
            raspuns = input("introduceti raspunsul: ")
            if raspuns == "3":
                print("Raspuns corect!")
                scor += 1
                score.clear()
                score.write(f"Score: {scor}", align='center', font=style2)
                break
            else:
                print("Raspuns gresit!")
                break
        elif intrebare == 2:
            pix.write(f"1. Daca fixam o axa Ox pe diametrul cercului ce miscare va avea corpul?", move=True, align='center', font=style1)
            raspuns = input("Introduceti raspunsul: ")
            if raspuns == "Miscare oscilatorie":
                print("Raspuns corect!")
                scor += 1
                score.clear()
                score.write(f"Score: {scor}", align='center', font=style2)
                break
            else:
                print("Raspuns gresit!")
                break
        elif intrebare == 3:
            pix.write(f"1. Unitatea de masura pentru FORTA este?", move=True, align='center', font=style1)
            raspuns = input("introduceti raspunsul: ")
            if raspuns == "Newton":
                print("Raspuns corect!")
                scor += 1
                score.clear()
                score.write(f"Score: {scor}", align='center', font=style2)
                break
            else:
                print("Raspuns gresit!")
                break
            
pix1 = turtle.Turtle()
pix1.hideturtle()
pix1.color('#3CFE01')
pix1.penup()
pix1.goto(0, 60)
pix1.pendown()

def intrebare2(x):
    while True:
        global scor
        intrebare = x
        if intrebare == 1:
            pix1.write(f"2. Ce marime constanta are GREUTATEA in formula sa?", move=True, align='center', font=style1)
            raspuns = input("Introduceti raspunsul: ")
            if raspuns == "Acceleratia gravitationala":
                print("Raspuns corect!")
                scor += 1
                score.clear()
                score.write(f"Score: {scor}", align='center', font=style2)
                break
            else:
                print("Raspuns gresit!")
                break
        elif intrebare == 2:
            pix1.write(f"2. Ec_i = Ep_f si Ep_i = Ec_f daca si numai daca fortele sunt?", move=True, align='center', font=style1)
            raspuns = input("Introduceti raspunsul: ")
            if raspuns == "Conservative":
                print("Raspuns corect!")
                scor += 1
                score.clear()
                score.write(f"Score: {scor}", align='center', font=style2)
                break
            else:
                print("Raspuns gresit!")
                break
        elif intrebare == 3:
            pix1.write(f"2. Unitatea de masura a ENERGIEI este?", move=True, align='center', font=style1)
            raspuns = input("Introduceti raspunsul: ")
            if raspuns == "Joule":
                print("Raspuns corect!")
                scor += 1
                score.clear()
                score.write(f"Score: {scor}", align='center', font=style2)
                break
            else:
                print("Raspuns gresit!")
                break

pix2 = turtle.Turtle()
pix2.hideturtle()
pix2.color('#3CFE01')
pix2.penup()
pix2.goto(0, 20)
pix2.pendown()

def intrebare3(x):
    while True:
        global scor
        intrebare = x
        if intrebare == 1:
            pix2.write(f'3. Legea lui Ohm este: "Daca esti om cu mine, sunt om cu tine"? (Da sau Nu):', move=True, align='center', font=style1)
            raspuns = input("Introduceti raspunsul: ")
            if raspuns == "Nu":
                print("Raspuns corect!")
                scor += 1
                score.clear()
                score.write(f"Score: {scor}", align='center', font=style2)
                break
            else:
                print("Raspuns gresit!")
                break
        elif intrebare == 2:
            pix2.write(f'3. De ce depinde forta de frecare?', move=True, align='center', font=style1)
            raspuns = input("Introduceti raspunsul: ")
            if raspuns == "Natura suprafetei":
                print("Raspuns corect!")
                scor += 1
                score.clear()
                score.write(f"Score: {scor}", align='center', font=style2)
                break
            else:
                print("Raspuns gresit!")
                break
        elif intrebare == 3:
            pix2.write(f'3. Purtătorii de sarcină mobili dintr-un metal sunt?', move=True, align='center', font=style1)
            raspuns = input("Introduceti raspunsul: ")
            if raspuns == "Electronii":
                print("Raspuns corect!")
                scor += 1
                score.clear()
                score.write(f'Score: {scor}', align='center', font=style2)
                break
            else:
                print("Raspuns gresit!")
                break

pix3 = turtle.Turtle()
pix3.hideturtle()
pix3.color('#3CFE01')
pix3.penup()
pix3.goto(0, -20)
pix3.pendown()

def intrebare4(x):
    while True:
        global scor
        intrebare = x
        if intrebare == 1:
            pix3.write(f'4. In miscarea rectilinie si uniforma, mobilul are?', move=True, align='center', font=style1)
            raspuns = input("Introduceti raspunsul: ")
            if raspuns == "Viteza constanta":
                print("Raspuns corect!")
                scor += 1
                score.clear()
                score.write(f'Score: {scor}', align='center', font=style2)
                break
            else:
                print('Raspuns gresit!')
                break
        if intrebare == 2:
            pix3.write(f'4. In miscarea rectilinie si variata, mobilul are?', move=True, align='center', font=style1)
            raspuns=input('Introduceti raspunsul: ')
            if raspuns == "Acceleratie constanta":
                print("Raspuns corect")
                scor += 1
                score.clear()
                score.write(f'Score: {scor}', align='center', font=style2)
                break
            else:
                print("Raspuns gresit!")
                break
        if intrebare == 3:
            pix3.write(f'4. Cum se numeste forta cu care corpul apasa pe o suprafata orizontala?', move=True, align='center',font=style1)
            raspuns=input("Introduceti raspunsul: ")
            if raspuns == "Greutatea":
                print("Raspuns corect!")
                scor += 1
                score.clear()
                score.write(f"Score: {scor}", align='center', font=style2)
                break
            else:
                print('Raspuns gresit!')
                break

pix4 = turtle.Turtle()
pix4.hideturtle()
pix4.color('#3CFE01')
pix4.penup()
pix4.goto(0, -60)
pix4.pendown()

def intrebare5(x):
    while True:
        global scor
        intrebare = x
        if intrebare == 1:
            pix4.write(f'5. Daca un corp este in cadere, acceleratia acestuia va fi egala cu?', move=True, align='center',font=style1)
            raspuns = input("Introduceti raspunsul: ")
            if raspuns == "Acceleratia gravitationala":
                print("Raspuns corect!")
                scor += 1
                score.clear()
                score.write(f"Score: {scor}", align='center', font=style2)
                break
            else:
                print('Raspuns gresit!')
                break
        elif intrebare == 2:
            pix4.write(f'5. Ce produce ciocnirea PLASTICA?', move=True, align='center',font=style1)
            raspuns=input("Introduceti raspunsul: ")
            if raspuns == "Caldura":
                print("Raspuns corect!")
                scor += 1
                score.clear()
                score.write(f'Score: {scor}', align='center', font=style2)
                break
            else:
                print("Raspuns gresit!")
                break
        elif intrebare == 3:
            pix4.write(f'5. Ce tip de lentila este lupa?', move=True, align='center',font=style1)
            raspuns=input("Introduceti raspunsul: ")
            if raspuns == "Convergenta":
                print("Raspuns corect!")
                scor += 1
                score.clear()
                score.write(f'Score: {scor}', align='center', font=style2)
                break
            else:
                print("Raspuns gresit!")
                break

pix5 = turtle.Turtle()
pix5.hideturtle()
pix5.color('#FEFEFE')
pix5.penup()
pix5.goto(0, -320)
pix5.pendown()

def Rezultat():
    global scor
    if scor >= 3:
        pix5.write(f'Felicitari, ati invatat bine!', move=True, align='center',font=style)
    else:
        pix5.write(f'Ati pierdut, mai aveti de invatat!', move=True, align='center', font=style)
        
        

def Run_Menu():
    numar = random.randrange(1, 4, 1)
    intrebare1(numar)
    intrebare2(numar)
    intrebare3(numar)
    intrebare4(numar)
    intrebare5(numar)
    Rezultat()
Run_Menu()
            




display.update()
