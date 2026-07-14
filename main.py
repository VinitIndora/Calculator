import customtkinter as ctk


#  SETTINGS 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.title("Glass Calculator")
app.geometry("420x650")
app.resizable(False, False)

# Window transparency
app.attributes("-alpha", 0.96)

# Background
app.configure(fg_color="#101010")


# DISPLAY

display = ctk.CTkEntry(
    app,
    height=90,
    font=("Arial", 34, "bold"),
    justify="right",
    text_color="white",
    fg_color="#1f1f1f",
    corner_radius=25
)

display.pack(
    padx=25,
    pady=30,
    fill="x"
)


#  FUNCTION

def press(value):
    display.insert("end", value)


def clear():
    display.delete(0, "end")


def backspace():
    text = display.get()
    display.delete(0, "end")
    display.insert(0, text[:-1])


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, "end")
        display.insert(0, str(result))

    except:
        display.delete(0, "end")
        display.insert(0, "Error")


#  GLASS PANEL 

panel = ctk.CTkFrame(
    app,
    width=360,
    height=400,
    corner_radius=35,
    fg_color="#202020"
)

panel.pack(
    padx=20,
    pady=10
)


#  BUTTON CREATOR 

def create_button(text, row, col, color="#333333", command=None):

    button = ctk.CTkButton(
        panel,
        text=text,
        width=75,
        height=75,
        corner_radius=22,
        font=("Arial", 22, "bold"),
        fg_color=color,
        hover_color=color,
        text_color="white",
        command=command
    )

    button.grid(
        row=row,
        column=col,
        padx=8,
        pady=8
    )


    # Cursor enter animation
    def on_enter(event):
        animate_color(button, "#00aaff")


    # Cursor leave animation
    def on_leave(event):
        animate_color(button, color)


    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    return button



# Smooth color animation
def animate_color(widget, target):

    current = widget.cget("fg_color")

    widget.configure(
        fg_color=target
    )


#  NUMBER BUTTONS 

buttons = [
    ("7",0,0), ("8",0,1), ("9",0,2), ("/",0,3),
    ("4",1,0), ("5",1,1), ("6",1,2), ("*",1,3),
    ("1",2,0), ("2",2,1), ("3",2,2), ("-",2,3),
    ("0",3,0), (".",3,1), ("+",3,2)
]


for text,row,col in buttons:
    create_button(
        text,
        row,
        col,
        command=lambda x=text: press(x)
    )


# Equal button

create_button(
    "=",
    3,
    3,
    color="#00a86b",
    command=calculate
)


# CONTROL BUTTONS 

ctk.CTkButton(
    app,
    text="CLEAR",
    width=200,
    height=45,
    corner_radius=20,
    font=("Arial",18,"bold"),
    fg_color="#d93025",
    hover_color="#ff6659",
    command=clear
).pack(pady=10)



ctk.CTkButton(
    app,
    text="⌫ BACKSPACE",
    width=200,
    height=45,
    corner_radius=20,
    font=("Arial",18,"bold"),
    fg_color="#f9ab00",
    hover_color="#ffd166",
    command=backspace
).pack()


# Keyboard support

def keyboard_input(event):

    if event.char in "0123456789+-*/.":
        press(event.char)

    elif event.keysym == "Return":
        calculate()

    elif event.keysym == "BackSpace":
        backspace()


app.bind("<Key>", keyboard_input)


# Start app
app.mainloop()