import tkinter as tk

# function to draw lines

def draw(event):
x1, y1 = (event.x - 1), (event.y -1) #Starting Point
x2, y2 = (event.x  +1), (event.y +1) #Ending Point

# Set up the main window

root = tk.Tk()
root.title("Simple drawing tool")

# Creates a canvas widget where you draw

canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

# Mouse movement
canvas.bind("<B1-Motion>", draw)
canvas.bind("<Stop Drawing>",  lambda event: None)

# Delete Button
def clear_canvas():
canvas.delete("all")
clear_button = tk.Button(root, text="Clear Canvases", command=clear_canvas)
clear_button.pack()

# Drawing Libary Loop
root.mainloop()
