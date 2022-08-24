import math
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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_title.config(text="Timer", fg=GREEN)
    checked.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global timer

    global reps
    reps += 1

    work = 60 * WORK_MIN
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        label_title.config(text="20 min break!", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        label_title.config(text="5 min break!", fg=PINK)
    else:
        count_down(work)
        label_title.config(text="Work time!", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    minutes = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    time = f"{minutes}:{sec}"

    canvas.itemconfig(timer_text, text=time)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        check = ""
        for _ in range(math.floor(reps/2)):
            check += "🗹"
        checked.config(text="🗹")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)

label_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
label_title.grid(row=1, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=1)

# Start
button_start = Button(text="Start", command=start_timer, border=0, font=(FONT_NAME, 12, "bold"))
button_start.grid(row=3, column=0)

# Reset
button_reset = Button(text="Reset", command=timer_reset, border=0, font=(FONT_NAME, 12, "bold"))
button_reset.grid(row=3, column=2)

checked = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18, "bold"))
checked.grid(row=4, column=1)

window.mainloop()
