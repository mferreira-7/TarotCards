import random
import tkinter
import tkinter.messagebox
import requests
import json

BASE_URL = "https://tarotapi.dev/api/v1/cards/"

#Dict of card long and short names for api call
tarot = {
    "The Magician": "ar01", 
    "The High Priestess": "ar02", 
    "The Empress": "ar03", 
    "The Emperor": "ar04", 
    "The Hierophant": "ar05", 
    "The Lovers": "ar06", 
    "The Chariot": "ar07", 
    "Strength": "ar08", 
    "The Hermit": "ar09", 
    "Wheel of Fortune": "ar10", 
    "Justice": "ar11", 
    "The Hanged Man": "ar12", 
    "Death": "ar13", 
    "Temperance": "ar14", 
    "The Devil": "ar15", 
    "The Tower": "ar16", 
    "The Star": "ar17", 
    "The Moon": "ar18", 
    "The Sun": "ar19", 
    "The Last Judgement": "ar20", 
    "The World": "ar21", 
    "The Fool": "ar00"
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

        resultBox1.replace(1.0, "end", "Your past card is: " + cards["past"])
        resultBox1.config(state = 'disabled')

        resultBox2.replace(1.0, "end", "Your present card is: " + cards["present"])
        resultBox2.config(state = 'disabled')

        resultBox3.replace(1.0, "end", "Your future card is: " + cards["future"])
        resultBox3.config(state = 'disabled')

        drawButton.destroy()
        textBind()
    except:
        drawCards()       

def getCardDescription(cardShortName):
    response = requests.get(BASE_URL + cardShortName)
    cardData = response.json()
    return str(cardData['card']['meaning_up'])

def onClick(event):        
    match str(event.widget):
        case ".!text":
            card = resultBox1.get(1.0, "end")[:-1].lstrip("Your past card is: ")
            tkinter.messagebox.showinfo(card + " Description", getCardDescription(tarot[card])) 
        case ".!text2":
            card = resultBox2.get(1.0, "end")[:-1].lstrip("Your present card is: ")
            tkinter.messagebox.showinfo(card + " Description", getCardDescription(tarot[card])) 
        case ".!text3":
            card = resultBox3.get(1.0, "end")[:-1].lstrip("Your future card is: ")
            tkinter.messagebox.showinfo(card + " Description", getCardDescription(tarot[card])) 

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