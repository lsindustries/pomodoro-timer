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
def

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


label_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label_title.grid(row=1, column=1)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=1)
button_start = Button(text="Start", background=YELLOW, border=0, font=(FONT_NAME, 12, "bold"))
button_start.grid(row=3, column=0)
button_reset = Button(text="Reset", background=YELLOW, border=0, font=(FONT_NAME, 12, "bold"))
button_reset.grid(row=3, column=2)
checked = Label(text="🗹", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18, "bold"))
checked.grid(row=4, column=1)

window.mainloop()