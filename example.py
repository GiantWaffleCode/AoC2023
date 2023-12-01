import tkinter as tk

var1 = 'TEST'
print(f'{var1}')

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
canvas.create_rectangle(0,0,10,10, fill='red')
root.mainloop()