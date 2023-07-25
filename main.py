from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer, text="00:00")
    text.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    # countdown(300)

    if reps % 8 == 0:
        countdown(long_break_secs)
        # reps = 0
        text.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_secs)
        text.config(text="Short break", fg=PINK)
    else:
        countdown(work_secs)
        text.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# count = 5


def countdown(count):

    minutes = math.floor(count/60)
    sec = count % 60
    if sec == 0:
        sec = "00"
    elif sec <= 9:
        sec = f"0{sec}"
    else:
        sec = sec

    canvas.itemconfig(timer, text=f"{minutes}:{sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, countdown, count -1)
    else:
        start_timer()
        check = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            check += "✔"
        check_mark.config(text= check)

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
timer = canvas.create_text(103, 120, text="00:00", fill="white", font=(FONT_NAME, 30, "italic") )
canvas.grid(column=1, row=1)

# buttons
start_btn = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=3)

reset_btn = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_btn.grid(column=3, row=3)

# check mark
check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
check_mark.grid(column=1, row=3)

window.mainloop()