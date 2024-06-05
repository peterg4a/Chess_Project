import tkinter as tk
from PIL import Image, ImageTk

def on_image_click(event):
    canvas.scan_mark(event.x, event.y)

def on_image_drag(event):
    canvas.scan_dragto(event.x, event.y, gain=1)

root = tk.Tk()
root.title("Multiple Drag and Drop Images")
root.geometry("800x600")

image_paths = ["Chess/pieces/bbishop.png"]  # Add more paths as needed
images = [Image.open(path).convert("RGBA").resize((100,100)) for path in image_paths]
tk_images = [ImageTk.PhotoImage(image) for image in images]

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

image_ids = [canvas.create_image(100 + i * 200, 100, anchor=tk.NW, image=tk_image) for i, tk_image in enumerate(tk_images)]

for image_id in image_ids:
    canvas.tag_bind(image_id, "<ButtonPress-1>", on_image_click)
    canvas.tag_bind(image_id, "<B1-Motion>", on_image_drag)

root.mainloop()