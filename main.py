from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
# window.minsize(width=500, height=350)
# create canvas
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)

# title text
text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
text.grid(column=1, row=0)

# add img
img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=img)
canvas.create_text(103, 120, text="00:00", fill="white", font=(FONT_NAME, 30, "italic") )
canvas.grid(column=1, row=1)

# buttons
start_btn = Button(text="Start", bg=YELLOW, highlightthickness=0)
start_btn.grid(column=0, row=3)

reset_btn = Button(text="Reset", bg=YELLOW, highlightthickness=0)
reset_btn.grid(column=3, row=3)

# check mark
check_mark = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
check_mark.grid(column=1, row=3)

window.mainloop()