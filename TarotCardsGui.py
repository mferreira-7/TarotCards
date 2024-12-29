import random
import tkinter
import tkinter.messagebox

#Dict of card names and definitions
tarot = {
    "The Magician": "TheMagicianDesc", 
    "The High Priestess": "TheHighPriestessDesc", 
    "The Empress": "TheEmpressDesc", 
    "The Emperor": "TheEmperorDesc", 
    "The Hierophant": "TheHierophantDesc", 
    "The Lovers": "TheLoversDesc", 
    "The Chariot": "TheChariotDesc", 
    "Strength": "StrengthDesc", 
    "The Hermit": "TheHermitDesc", 
    "Wheel of Fortune": "WheelofFortuneDesc", 
    "Justice": "JusticeDesc", 
    "The Hanged Man": "TheHangedManDesc", 
    "Death": "DeathDesc", 
    "Temperance": "TemperanceDesc", 
    "The Devil": "TheDevilDesc", 
    "The Tower": "TheTowerDesc", 
    "The Star": "TheStarDesc", 
    "The Moon": "TheMoonDesc", 
    "The Sun": "TheSunDesc", 
    "Judgement": "JudgementDesc", 
    "The World": "TheWorldDesc", 
    "The Fool": "TheFoolDesc"
}

#Initialise Window
root=tkinter.Tk()
root.title("Tarot Cards by Marcel")
root.geometry("400x320")

#Create GUI
resultBox1 = tkinter.Text(root, height=2, width=30, font=("Arial", 24))
resultBox1.insert(1.0,"Press the button to draw 3 cards")
resultBox1.pack()

resultBox2 = tkinter.Text(root, height=2, width=30, font=("Arial", 24))
resultBox2.insert(1.0,"")
resultBox2.pack()

resultBox3 = tkinter.Text(root, height=2, width=30, font=("Arial", 24))
resultBox3.insert(1.0,"")
resultBox3.pack()

def drawCards():
    try:
        card1 = random.randint(0, 23)
        card2 = random.randint(0, 23)
        card3 = random.randint(0, 23)

        cards = {}
        cards["past"] = list(tarot)[card1]
        cards["present"] = list(tarot)[card2]
        cards["future"] = list(tarot)[card3]

        resultBox1.replace(1.0, "end", cards["past"])
        resultBox2.replace(1.0, "end", cards["present"])
        resultBox3.replace(1.0, "end", cards["future"])

        drawButton.destroy()
        textBind()
    except:
        drawCards()       

def onClick(event):        
    match str(event.widget):
        case ".!text":
            card = resultBox1.get(1.0, "end")[:-1]
            print(tarot[card])
        case ".!text2":
            card = resultBox2.get(1.0, "end")[:-1]
            print(tarot[card])
        case ".!text3":
            card = resultBox3.get(1.0, "end")[:-1]
            print(tarot[card])

def textBind():
    resultBox1.bind("<Button-1>", onClick)
    resultBox2.bind("<Button-1>", onClick)
    resultBox3.bind("<Button-1>", onClick)

    drawButtonReplacement = tkinter.Button(root, text="Click on a card to get its description", width=10, height=10)
    drawButtonReplacement.pack(side="bottom", fill="x")

#Create button
drawButton = tkinter.Button(root, command=lambda:drawCards(), text="Draw Cards", width=10, height=10)
drawButton.pack(side="bottom", fill="x")

root.mainloop()