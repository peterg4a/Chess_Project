import tkinter as tk
from PIL import Image, ImageTk

# Size of each square
size = 60

# Initialize the global variables
current_image = None
start_x = 0
start_y = 0

def on_image_click(event):
    global current_image, start_x, start_y
    # Get the ID of the currently clicked image
    current_image = event.widget.find_withtag("current")[0]
    # Store the initial position of the mouse click
    start_x = event.x
    start_y = event.y
def on_image_drag(event):
    global start_x, start_y
    # Calculate the distance moved
    dx = event.x - start_x
    dy = event.y - start_y
    # Move the current image by the distance moved
    canvas.move(current_image, dx, dy)
    # Update the starting position for the next movement
    start_x = event.x
    start_y = event.y
def on_image_release(event):
    global start_x, start_y
    canvas.moveto(current_image, (start_x//size)*size, (start_y//size)*size)

root = tk.Tk()
root.title("Multiple Drag and Drop Images with Transparency")
root.geometry("800x600")

image_paths = ["Chess/pieces/bbishop.png","Chess/pieces/wbishop.png"]  # Add more paths as needed
images = [Image.open(path).convert("RGBA").resize((size,size)) for path in image_paths]
tk_images = [ImageTk.PhotoImage(image) for image in images]

canvas = tk.Canvas(root, width=size*8, height=size*8)
canvas.pack()

# Draw the squares of the board
color = True
for x in range(8):
    for y in range(8):
        if (x+y)%2 != 0:
            canvas.create_rectangle(x*size, y*size, x*size+size, y*size+size, fill='white')
        else:
            canvas.create_rectangle(x*size, y*size, x*size+size, y*size+size, fill='brown')
        color = not color

# Place the images on the canvas and keep references to the image objects
image_ids = [canvas.create_image(100 + i * 200, 100, anchor=tk.NW, image=tk_image) for i, tk_image in enumerate(tk_images)]

# Bind the event handlers to each image for dragging functionality
for image_id in image_ids:
    canvas.tag_bind(image_id, "<ButtonPress-1>", on_image_click)
    canvas.tag_bind(image_id, "<B1-Motion>", on_image_drag)
    canvas.tag_bind(image_id, "<ButtonRelease-1>", on_image_release)

root.mainloop()
