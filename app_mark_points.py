import tkinter as tk
from tkinter import simpledialog, filedialog
from PIL import Image, ImageTk

# List to store marked points and line references
points = []
lines = []
drawing = False
erasing = False
marking_points = False

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((400, 400))
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        canvas.image = img_tk

def start_draw(event):
    global drawing
    drawing = True
    points.append((event.x, event.y))

def draw(event):
    if drawing:
        x, y = event.x, event.y
        points.append((x, y))
        line = canvas.create_line(points[-2], points[-1], fill="blue", width=2)
        lines.append(line)

def stop_draw(event):
    global drawing
    drawing = False
    points.clear()

def start_erase(event):
    global erasing
    erasing = True

def erase(event):
    if erasing:
        x, y = event.x, event.y
        items = canvas.find_overlapping(x-5, y-5, x+5, y+5)
        for item in items:
            if item in lines:
                canvas.delete(item)
                lines.remove(item)

def stop_erase(event):
    global erasing
    erasing = False

def mark_point(event):
    x, y = event.x, event.y
    point_name = simpledialog.askstring("Input", "Enter point name:")
    if point_name:
        point = canvas.create_oval(x-3, y-3, x+3, y+3, fill="red")
        text = canvas.create_text(x, y-10, text=point_name, fill="black")
        points.append((point, text))

def set_draw_mode():
    global drawing, erasing, marking_points
    drawing = True
    erasing = False
    marking_points = False
    canvas.bind("<Button-1>", start_draw)
    canvas.bind("<B1-Motion>", draw)
    canvas.bind("<ButtonRelease-1>", stop_draw)
    canvas.unbind("<Button-3>")
    canvas.unbind("<B3-Motion>")
    canvas.unbind("<ButtonRelease-3>")

def set_erase_mode():
    global drawing, erasing, marking_points
    drawing = False
    erasing = True
    marking_points = False
    canvas.bind("<Button-1>", start_erase)
    canvas.bind("<B1-Motion>", erase)
    canvas.bind("<ButtonRelease-1>", stop_erase)
    canvas.unbind("<Button-3>")
    canvas.unbind("<B3-Motion>")
    canvas.unbind("<ButtonRelease-3>")

def set_mark_point_mode():
    global drawing, erasing, marking_points
    drawing = False
    erasing = False
    marking_points = True
    canvas.bind("<Button-1>", mark_point)
    canvas.unbind("<B1-Motion>")
    canvas.unbind("<ButtonRelease-1>")
    canvas.unbind("<Button-3>")
    canvas.unbind("<B3-Motion>")
    canvas.unbind("<ButtonRelease-3>")

def undo_last_action():
    if marking_points and points:
        point, text = points.pop()
        canvas.delete(point)
        canvas.delete(text)
    elif drawing and lines:
        line = lines.pop()
        canvas.delete(line)

root = tk.Tk()
root.title("Thullex")

# Upload button
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

# Draw button
draw_button = tk.Button(root, text="Draw", command=set_draw_mode)
draw_button.pack()

# Erase button
erase_button = tk.Button(root, text="Erase", command=set_erase_mode)
erase_button.pack()

# Mark Point button
mark_point_button = tk.Button(root, text="Mark Point", command=set_mark_point_mode)
mark_point_button.pack()

# Undo button
undo_button = tk.Button(root, text="Undo", command=undo_last_action)
undo_button.pack()

# Canvas for drawing
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

root.mainloop()