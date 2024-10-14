from tkinter import *
import subprocess
import threading

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

        # Print the currently entered command instantly in the custom terminal
        command_label = Label(window, text="_> " + user_input_var, font=("monospace", 12), fg='#00FF00', bg='black', anchor="w")
        command_label.grid(column=0, row=current_row, columnspan=2, sticky="w")
        current_row += 1  # Only increment row after adding the command label

        # Run the command in a separate thread to avoid blocking the GUI
        threading.Thread(target=run_command, args=(user_input_var,)).start()

    # Move the entry to a new row with the prompt '_>' for new input
    new_prompt_label = Label(window, text="_>", font=("monospace", 12), fg='#00FF00', bg='black', anchor="w")
    new_prompt_label.grid(column=0, row=current_row, sticky="w")

    # Re-position the entry field below the new prompt
    entry.grid(column=1, row=current_row, sticky="w")
    entry.focus()

# Function to execute the command and display the output in the GUI
def run_command(command):
    global current_row
    try:
        # Execute the command using subprocess
        result = subprocess.run(command, capture_output=True, shell=True, text=True)
        output = result.stdout.strip()  # Capture the output of the command
        error = result.stderr.strip()  # Capture any error messages

        # Display the output in the custom terminal, left-aligned
        if output:
            output_label = Label(window, text=output, font=("monospace", 12), fg='#00FF00', bg='black', anchor="w", justify="left")
            output_label.grid(column=0, row=current_row, columnspan=2, sticky="w")
            current_row += 1
        if error:
            error_label = Label(window, text=error, font=("monospace", 12), fg='red', bg='black', anchor="w", justify="left")
            error_label.grid(column=0, row=current_row, columnspan=2, sticky="w")
            current_row += 1

    except Exception as e:
        error_label = Label(window, text=str(e), font=("monospace", 12), fg='red', bg='black', anchor="w", justify="left")
        error_label.grid(column=0, row=current_row, columnspan=2, sticky="w")
        current_row += 1

# Initial label for the first prompt
lb = Label(window, text="_>", font=("monospace", 12), fg='#00FF00', bg='black', anchor="w")
lb.grid(column=0, row=current_row, sticky="w")

# Input entry field
entry = Entry(window, width=50, font=("monospace", 12), fg='#00FF00', bg='black', insertbackground='#00FF00', highlightthickness=0, borderwidth=0)
entry.grid(column=1, row=current_row, sticky="w")
entry.bind("<Return>", get_user_input)

entry.focus()  # Automatically focus on entry when the window opens

window.mainloop()
