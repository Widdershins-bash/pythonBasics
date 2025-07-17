from tkinter import *

def convert_miles():
    converted_label.config(text=float(miles_input.get()) * 1.60934)

def create_label(grid_column, grid_row, text):
    new_label = Label(text=text, padx=5, pady= 5)
    new_label.grid(column=grid_column, row=grid_row)

    return new_label

#window
window = Tk()
window.title("mi to km")
window.config(padx=20, pady=20)

#input
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

#button
convert_button = Button(text="convert", command=convert_miles)
convert_button.grid(column=1, row=2)

#labels
mi_label = create_label(grid_column=2, grid_row=0, text="Miles")
km_label = create_label(grid_column=2, grid_row=1, text="Km")
info_label = create_label(grid_column=0, grid_row=1, text="is equal to")
converted_label = create_label(grid_column=1, grid_row=1, text="0")

window.mainloop()
