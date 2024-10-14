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

# Function to auto-scroll to the bottom
def auto_scroll():
    canvas.update_idletasks()
    canvas.yview_moveto(1.0)

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
        command_label = Label(scrollable_frame, text="_> " + user_input_var, font=("monospace", 12), fg='#00FF00', bg='black', anchor="w")
        command_label.grid(column=0, row=current_row, columnspan=2, sticky="w")
        current_row += 1  # Increment row after adding the command label

        # Run the command in a separate thread to avoid blocking the GUI
        threading.Thread(target=run_command, args=(user_input_var,)).start()

    # Move the entry to a new row with the prompt '_>' for new input
    new_prompt_label = Label(scrollable_frame, text="_>", font=("monospace", 12), fg='#00FF00', bg='black', anchor="w")
    new_prompt_label.grid(column=0, row=current_row, sticky="w")

    # Re-position the entry field below the new prompt
    entry.grid(column=1, row=current_row, sticky="w")
    entry.focus()

    # Auto-scroll to the bottom
    window.after(100, auto_scroll)

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
            output_label = Label(scrollable_frame, text=output, font=("monospace", 12), fg='#00FF00', bg='black', anchor="w", justify="left", wraplength=500)
            output_label.grid(column=0, row=current_row, columnspan=2, sticky="w")
            current_row += 1
        if error:
            error_label = Label(scrollable_frame, text=error, font=("monospace", 12), fg='red', bg='black', anchor="w", justify="left", wraplength=500)
            error_label.grid(column=0, row=current_row, columnspan=2, sticky="w")
            current_row += 1

    except Exception as e:
        error_label = Label(scrollable_frame, text=str(e), font=("monospace", 12), fg='red', bg='black', anchor="w", justify="left", wraplength=500)
        error_label.grid(column=0, row=current_row, columnspan=2, sticky="w")
        current_row += 1

    # After command execution, create a new prompt
    new_prompt_label = Label(scrollable_frame, text="_>", font=("monospace", 12), fg='#00FF00', bg='black', anchor="w")
    new_prompt_label.grid(column=0, row=current_row, sticky="w")

    # Re-position the entry field below the new prompt
    entry.grid(column=1, row=current_row, sticky="w")
    entry.focus()

    # Auto-scroll to the bottom
    window.after(100, auto_scroll)

# Create a canvas and scrollbar
canvas = Canvas(window, bg='black', highlightthickness=0)
scrollbar = Scrollbar(window, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas, bg='black')

# Configure the canvas
canvas.configure(yscrollcommand=scrollbar.set)
scrollable_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a window inside the canvas which will be scrolled with it
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Use grid for main layout
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
canvas.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

# Initial label for the first prompt
lb = Label(scrollable_frame, text="_>", font=("monospace", 12), fg='#00FF00', bg='black', anchor="w")
lb.grid(column=0, row=current_row, sticky="w")

# Input entry field
entry = Entry(scrollable_frame, width=50, font=("monospace", 12), fg='#00FF00', bg='black', insertbackground='#00FF00', highlightthickness=0, borderwidth=0)
entry.grid(column=1, row=current_row, sticky="w")
entry.bind("<Return>", get_user_input)

entry.focus()  # Automatically focus on entry when the window opens

# Bind mousewheel to scrolling
def on_mousewheel(event):
    canvas.yview_scroll(-1 * int(event.delta / 120), "units")

canvas.bind_all("<MouseWheel>", on_mousewheel)

# Bind arrow keys to scrolling
def on_up_arrow(event):
    canvas.yview_scroll(-1, "units")

def on_down_arrow(event):
    canvas.yview_scroll(1, "units")

window.bind("<Up>", on_up_arrow)
window.bind("<Down>", on_down_arrow)

window.mainloop()