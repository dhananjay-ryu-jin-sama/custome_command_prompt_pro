from tkinter import *

window = Tk()

window.title("Pokemon")
window.geometry('540x300')
window.configure(bg='black')

user_input_var = ""

def get_user_input(event):
    global user_input_var
    user_input_var = entry.get()
    entry.delete(0, END)
    print("You entered:", user_input_var)

lb = Label(window, text="_>", font=("monospace", 12), fg='#00FF00', bg='black')
lb.grid(column=0, row=0)

entry = Entry(window, width=50, font=("monospace", 12), fg='#00FF00', bg='black', insertbackground='#00FF00', highlightthickness=0, borderwidth=0)
entry.grid(column=1, row=0)
entry.bind("<Return>", get_user_input)

window.mainloop()