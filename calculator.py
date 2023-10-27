import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.title("Calculator")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")
entry.pack(fill=tk.BOTH, padx=10, pady=10, ipadx=8, ipady=8)

button_frame = tk.Frame(root)
button_frame.pack()

button_list = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row = 0
col = 0

for button_text in button_list:
    button = tk.Button(
        button_frame,
        text=button_text,
        font="lucida 15",
        padx=25,
        pady=5,
        relief=tk.RAISED,
        bd=5,
        background='yellow',
        foreground="WHITE"
    )
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
