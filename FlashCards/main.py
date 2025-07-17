from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    unknown_data = pandas.read_csv(r"data\unknown_words.csv")

except FileNotFoundError:
    original_data = pandas.read_csv(r"data\french_words.csv")
    card_words_dict = original_data.to_dict(orient='records')
        
else:
    card_words_dict = unknown_data.to_dict(orient='records')

random_index = random.choice(card_words_dict)

def next_word():
    global random_index, flip_timer
    window.after_cancel(flip_timer)
    random_index = random.choice(card_words_dict)
    card_canvas.itemconfig(image, image=card_front_image)
    card_canvas.itemconfig(card_title, text="French", fill="black")
    card_canvas.itemconfig(card_word, text=random_index['French'], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def known_word():
    card_words_dict.remove(random_index)
    unknown_word_df = pandas.DataFrame(card_words_dict)
    unknown_word_df.to_csv(r"data\unknown_words.csv", index=False)
    next_word()


def flip_card():
    card_canvas.itemconfig(image, image=card_back_image)
    card_canvas.itemconfig(card_title, text="English", fill="white")
    card_canvas.itemconfig(card_word, text=random_index['English'], fill="white")


def create_widget(widget_class, **kwargs):
    grid_options = {'columnspan' : kwargs.pop('columnspan', 1), 'column' : kwargs.pop('grid_x', 0), 'row' : kwargs.pop('grid_y', 0)}

    new_widget = widget_class(**kwargs)
    new_widget.grid(**grid_options)
    
    return new_widget

# ----------------------- GUI ---------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

right_image = PhotoImage(file=r"images\right.png")
wrong_image = PhotoImage(file=r"images\wrong.png")
card_back_image = PhotoImage(file=f"images\card_back.png")
card_front_image = PhotoImage(file=r"images\card_front.png")

card_canvas = create_widget(widget_class=Canvas, width=800, height=526, columnspan=2, bg=BACKGROUND_COLOR, highlightthickness=0)
image = card_canvas.create_image(400, 263, image=card_front_image)
card_title = card_canvas.create_text(400, 150, fill="black", font=("Ariel", 40, "italic"), text="French", tags="language_text")
card_word = card_canvas.create_text(400, 263, fill="black", font=("Ariel", 60, "bold"), text=random_index['French'], tags="word_text")

right_button = create_widget(widget_class=Button, grid_x=1, grid_y=1, image=right_image, highlightthickness=0,
                             activebackground=BACKGROUND_COLOR, borderwidth=0, command=known_word)
wrong_button = create_widget(widget_class=Button, grid_x=0, grid_y=1, image=wrong_image, highlightthickness=0,
                             activebackground=BACKGROUND_COLOR, borderwidth=0, command=next_word)

window.mainloop()
