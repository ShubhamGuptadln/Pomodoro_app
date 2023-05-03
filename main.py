from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.4
SHORT_BREAK_MIN = 0.2
LONG_BREAK_MIN = 0.3
reps = 0
timer=None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    canvas.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    mark_label.config(text="")
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    print(reps)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60



    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text='Long break', fg=RED, font=(FONT_NAME, 35, "bold"))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text='Short break', fg=PINK, font=(FONT_NAME, 35, "bold"))
    else:
        count_down(work_sec)
        timer_label.config(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time):
    min = math.floor(time / 60)
    sec = time % 60
    if min == 0:
        min = '00'

    if sec < 10:
        sec = f'0{sec}'
        if sec == 0:
            sec = "00"
    canvas.itemconfig(timer_text, text=f'{min}:{sec}')

    if time > 0:
        global  timer
        timer=window.after(1000, count_down, time - 1)
    else:
        start_timer()

        marks=""
        no_of_sessions=math.floor(reps/2)
        for i in range(no_of_sessions):
            marks+="✅"
        mark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=100, bg=YELLOW)
canvas = Canvas(height=200, width=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file='tomato.png')
canvas.create_image(103, 85, image=photo)
timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)
start_button = Button(text='Start', command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(row=2, column=2)

mark_label = Label( bg=YELLOW, fg=GREEN)
mark_label.grid(row=3, column=1)

window.mainloop()
