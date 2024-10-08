import json

marked_points = []

def mark_point(event):
    x, y = event.x, event.y
    point = {"id": f"marker_{len(marked_points) + 1}", "description": "Custom Point", "coordinates": [x, y]}
    marked_points.append(point)
    point_label = tk.Label(root, text=f"Point: ({x}, {y})", fg="red")
    point_label.place(x=x, y=y)

def save_markers():
    data = {
        "image_path": "path/to/uploaded/image.jpg",  # Replace with actual path
        "markers": marked_points
    }
    with open('markers.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print("Markers saved to markers.json")

# Add a Save button to the GUI
save_button = tk.Button(root, text="Save Markers", command=save_markers)
save_button.pack()
