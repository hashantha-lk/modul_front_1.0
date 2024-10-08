import json

# Define the structure for target values
target_values = {
    "B02 - Chest": {
        "label": "B02 - Chest",
        "description": "Measurement of chest width",
        "function": "measure_chest_width",
        "model": "yolo_chest_model",
        "line_color": [255, 0, 0],  # RGB color
        "dependencies": ["collar_point", "bottom_point"]
    },
    "C20 - Front Length": {
        "label": "C20 - Front Length",
        "description": "Length of the front",
        "function": "measure_front_length",
        "model": "yolo_front_model",
        "line_color": [0, 0, 255],  # RGB color
        "dependencies": ["collar_point", "bottom_point"]
    }
}

# Write the structure to a JSON file
with open('target_values.json', 'w') as json_file:
    json.dump(target_values, json_file, indent=4)

print("target_values.json has been created successfully!")
