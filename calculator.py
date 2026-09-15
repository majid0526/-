import tkinter as tk

def button_click(adad):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(adad))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        result = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "خطا")

root = tk.Tk()
root.title("ماشین حساب من")
root.geometry("320x400")

display = tk.Entry(root, font=("Arial", 24), justify="right", bd=10)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=("Arial", 18), command=button_equal)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 18),
                        command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

clear_btn = tk.Button(root, text="C", font=("Arial", 18), command=button_clear)
clear_btn.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()