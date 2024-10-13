from tkinter import *

window = Tk()

window.title("Pokemon Command Prompt")
window.geometry('540x400')
window.configure(bg='black')

current_row = 0  # Track the current row number
commands_list = []  # List to store all commands entered by the user
current_command = ""  # Variable to store the currently entered command

# Function to handle user input and create new prompt line
def get_user_input(event):
    global current_row, current_command
    user_input_var = entry.get()
    entry.delete(0, END)

    if user_input_var.strip():  # Check that the input isn't just whitespace
        # Add the user input to the commands list
        commands_list.append(user_input_var)
        current_command = user_input_var  # Store the latest command

        # Print the currently entered command instantly
        print("Current Command:", current_command)

        # Create a new label for the entered command
        command_label = Label(window, text="_> " + user_input_var, font=("monospace", 12), fg='#00FF00', bg='black')
        command_label.grid(column=0, row=current_row, columnspan=2, sticky="w")
        current_row += 1  # Only increment row after adding the command label

    # Move the entry to a new row with the prompt '_>' for new input
    new_prompt_label = Label(window, text="_>", font=("monospace", 12), fg='#00FF00', bg='black')
    new_prompt_label.grid(column=0, row=current_row, sticky="w")

    # Re-position the entry field below the new prompt
    entry.grid(column=1, row=current_row, sticky="w")
    entry.focus()

# Initial label for the first prompt
lb = Label(window, text="_>", font=("monospace", 12), fg='#00FF00', bg='black')
lb.grid(column=0, row=current_row, sticky="w")

# Input entry field
entry = Entry(window, width=50, font=("monospace", 12), fg='#00FF00', bg='black', insertbackground='#00FF00', highlightthickness=0, borderwidth=0)
entry.grid(column=1, row=current_row, sticky="w")
entry.bind("<Return>", get_user_input)

entry.focus()  # Automatically focus on entry when the window opens

window.mainloop()
