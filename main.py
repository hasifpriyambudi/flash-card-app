from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/Words_to_Learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
toLearn = data.to_dict(orient="records")
currentCard = {}


# Get Word France
def nextCard():
    global currentCard, flipTimer
    screen.after_cancel(flipTimer)
    currentCard = random.choice(toLearn)
    canvas.itemconfig(cardTitle, text="French", fill="Black")
    canvas.itemconfig(cardWord, text=currentCard["French"], fill="Black")
    canvas.itemconfig(cardBackground, image=cardFront)
    flipTimer = screen.after(2000, func=flipBack)


# Change English
def flipBack():
    canvas.itemconfig(cardBackground, image=cardBack)
    canvas.itemconfig(cardTitle, fill="White", text="English")
    canvas.itemconfig(cardWord, fill="White", text=currentCard["English"])


def isKnown():
    toLearn.remove(currentCard)
    newData = pandas.DataFrame(toLearn)
    newData.to_csv("data/Words_to_Learn.csv", index=False)
    print(len(toLearn))
    nextCard()


screen = Tk()
screen.title("Fiashy")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Change Card
flipTimer = screen.after(3000, flipBack)

# Card Front
cardFront = PhotoImage(file="images/card_front.png")
cardBack = PhotoImage(file="images/card_back.png")
cardBackground = canvas.create_image(400, 263, image=cardFront)
canvas.grid(column=0, row=0, columnspan=2)

# Button Check
imageCheck = PhotoImage(file="images/right.png")
buttonCheck = Button(image=imageCheck, highlightthickness=0, command=isKnown)
buttonCheck.grid(column=0, row=1)

# Button Wrong
imageWrong = PhotoImage(file="images/wrong.png")
buttonWrong = Button(image=imageWrong, highlightthickness=0, command=nextCard)
buttonWrong.grid(column=1, row=1)

# Label Language & Word
cardTitle = canvas.create_text(400, 150, fill="Black", font=("Arial", 40, "italic"))
cardWord = canvas.create_text(400, 263, fill="Black", font=("Arial", 60, "bold"))
nextCard()

screen.mainloop()
