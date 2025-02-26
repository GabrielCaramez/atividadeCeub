import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        result = eval(entry.get())
        messagebox.showinfo("Result", f"The result is: {result}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

app = tk.Tk()
app.title("Calculo simples")

label = tk.Label(app, text="adicione uma expreção:")
label.pack()

entry = tk.Entry(app)
entry.pack()

button = tk.Button(app, text="Calculate", command=calculate)
button.pack()

app.mainloop()