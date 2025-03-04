from tkinter import *
from pandas import *
import random

LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"

#Calling preferable data
try:
    word_data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_data = read_csv("data/french_words.csv")
    all_words = word_data.to_dict('records')
else:
    all_words = word_data.to_dict('records')



# color and lang change
def change():
    word = all_words[num]['English']
    canvas.itemconfig(label_language, text="English", fill='white')
    canvas.itemconfig(label_word, text=word, fill='white')
    canvas.itemconfig(canvas_image, image=card_back)

#removing card and calling draw function
def remove():
    try:
        del all_words[num]
    except:
        draw()

    finally:
        draw()
        data = DataFrame(all_words)
        data.to_csv('data/words_to_learn.csv', index=False)


# draw new word
def draw():
    global num
    num = random.randint(0, len(all_words))

    window.after(3000, change)

    word = all_words[num]['French']
    canvas.itemconfig(label_language, text="French", fill='black')
    canvas.itemconfig(label_word, text=word, fill='black')
    canvas.itemconfig(canvas_image, image=card_front)


window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashcards Project")

# Canvas
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")

canvas = Canvas(window, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 258, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

# Labels inside
label_language = canvas.create_text(400, 150, text="Title", font=LANGUAGE_FONT)
label_word = canvas.create_text(400, 263, text="Word", font=WORD_FONT)

x_photo = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_photo, highlightthickness=0, command=draw)
x_button.grid(row=1, column=0)

r_photo = PhotoImage(file="images/right.png")
r_button = Button(image=r_photo, highlightthickness=0, command=remove)
r_button.grid(row=1, column=1)

window.mainloop()
