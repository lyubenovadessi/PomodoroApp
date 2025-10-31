from selectors import SelectSelector
from tkinter import *
import math

COLORS = {"work":"#347433", "short": "#CC66DA", "long": "#004030", "bg": "#FCD8CD"}
FONT_NAME = "Courier"
TIMES = {"work": 25, "short": 5, "long": 25}

reps = 0
timer = ""

def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    title_label.config(text="TIMER", fg=COLORS["work"])
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")


def start_timer():
    global reps
    reps += 1

    session_type = (
        "long" if reps % 8 == 0 else
        "short" if reps % 2 == 0 else
        "work"
    )
    title_label.config(text = "BREAK" if session_type != "work" else "WORK", fg=COLORS[session_type])

    count_down(TIMES[session_type] * 60)


def count_down(count):
    mins, sec = divmod(count, 60)
    canvas.itemconfig(timer_text, text=f"{mins:02d}:{sec:02d}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = "✔️" * (reps // 2)
        check_marks.config(text=marks)


window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=COLORS["bg"])

title_label = Label(text="TIMER", fg=COLORS["work"], bg=COLORS["bg"], font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=397, height=396, bg=COLORS["bg"], highlightthickness=0)
tomato_img = PhotoImage(file="pomodoro_img.png")
canvas.create_image(198, 198, image=tomato_img)
timer_text = canvas.create_text(198, 220, text="00:00", fill="black", font=(FONT_NAME, 50, "bold"))
canvas.grid(column=1, row=1)

Button(text="Start", highlightthickness=0, command=start_timer).grid(column=0, row=2)
Button(text="Reset", highlightthickness=0, command=reset_timer).grid(column=2, row=2)

check_marks = Label(fg=COLORS["work"], bg=COLORS["bg"])
check_marks.grid(column=1, row=3)

window.mainloop()