import tkinter as tk
from PIL import Image, ImageTk
from Chess_back import *

def on_image_click(event):
    global current_image, prev_x, prev_y, start_x, start_y
    # Get the ID of the currently clicked image
    current_image = event.widget.find_withtag("current")[0]
    # Store the initial position of the mouse click
    start_x = (event.x//size)*size
    start_y = (event.y//size)*size
    prev_x = event.x
    prev_y = event.y
def on_image_drag(event):
    global prev_x, prev_y
    # Calculate the distance moved
    dx = event.x - prev_x
    dy = event.y - prev_y
    # Move the current image by the distance moved
    canvas.move(current_image, dx, dy)
    # Update the starting position for the next movement
    prev_x = event.x
    prev_y = event.y
def on_image_release(event):
    if 0 <= event.x and event.x <= 8*size and 0 <= event.y and event.y <= 8*size: #and islegal(start_x//size, start_y//size, (event.x//size)*size, (event.y//size)*size):
        canvas.moveto(current_image, (event.x//size)*size, (event.y//size)*size)
    else:
        canvas.moveto(current_image, start_x, start_y)

# Size of each square
size = 80

# Initialize the global variables
current_image = None
start_x = 0
start_y = 0
prev_x = 0
prev_y = 0

root = tk.Tk()
root.title("Chess")
root.geometry(str(size*8+5)+'x'+str(size*8+5))

image_paths = ["pieces/bbishop.png","pieces/wbishop.png"]  # Add more paths as needed
images = [Image.open(path).convert("RGBA").resize((size,size)) for path in image_paths]
tk_images = [ImageTk.PhotoImage(image) for image in images]

canvas = tk.Canvas(root, width=size*8, height=size*8)
canvas.pack()

# Draw the squares of the board
for x in range(8):
    for y in range(8):
        if (x+y)%2 != 0:
            canvas.create_rectangle(x*size, y*size, x*size+size, y*size+size, fill='white')
        else:
            canvas.create_rectangle(x*size, y*size, x*size+size, y*size+size, fill='brown')

# Place the images on the canvas and keep references to the image objects
image_ids = [canvas.create_image(100 + i * 200, 100, anchor=tk.NW, image=tk_image) for i, tk_image in enumerate(tk_images)]

# Bind the event handlers to each image for dragging functionality
for image_id in image_ids:
    canvas.tag_bind(image_id, "<ButtonPress-1>", on_image_click)
    canvas.tag_bind(image_id, "<B1-Motion>", on_image_drag)
    canvas.tag_bind(image_id, "<ButtonRelease-1>", on_image_release)

root.mainloop()
