from tkinter import *
import pandas as pd
import random


#----------------------------- CONSTANTS -----------------------------#
BACKGROUND_COLOR = "#B1DDC6"

#----------------------------- Generate Random Words -----------------------------#
data = pd.read_csv('data/french_words.csv')
french_words = data.to_dict(orient="records")

def generate_word():
   new_word= random.choice(french_words)
   canvas.itemconfig(word_to_learn, text= new_word["French"])
   canvas.itemconfig(lang, text="French")
#----------------------------- CANVAS UI -----------------------------#

window = Tk()
window.title("Language Learning Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height= 526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.gif")
canvas.create_image(405,262, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

#langugae label
lang = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_to_learn = canvas.create_text(400, 263, text="", font=("Ariel", 65, "bold"))



#--------------- BUTTONS ---------------#
confirm = PhotoImage(file="images/right.gif")
confirm_button = Button(image=confirm, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=generate_word)
confirm_button.grid(column=1, row=1)

wrong = PhotoImage(file="images/wrong.gif")
wrong_button = Button(image=wrong, highlightthickness=0, highlightbackground=BACKGROUND_COLOR )
wrong_button.grid(column=0, row=1)

generate_word()


window.mainloop()