objects = [
    "Accent Paving", "Barrier Post", "Barrier Stump", "Bench", "Bicycle", "Bridge", "Building", "Bus", "Bus Stop",
    "Car", "Chair", "Closed Sidewalk", "Counter", "Crosswalk", "Curb", "Dog", "Driveway(flat)", "Elevator",
    "Escalator", "Fence", "Fire hydrant", "Flush Door", "Foldout Sign", "Fountain", "Gate", "Guide dog", "Gutter",
    "Hose", "Lamp Post", "Mail box", "Maintenance Vehicle", "Motorcycle", "Parallel Parking Spot", "Paratransit vehicle",
    "Pedestrian Crossing", "Person", "Person with a disability", "Pillar", "Pole", "Puddle", "Push button", "Railing",
    "Raised Entryway", "Retaining Wall", "Road", "Road Divider", "Road Shoulder", "Roadside Parking", "Sidewalk",
    "Sidewalk pits", "Sign", "Sign Post", "Sloped Driveway", "Slopped Curb", "Snow", "Stairs", "Stop sign",
    "Street Vendor", "Table", "Tactile Paving", "Traffic Signals", "Train Platform", "Train Tracks", "Trash bins",
    "Trash on roads", "Tree", "Turnstile", "Uncontrolled Crossing", "Uneven Stairs", "Unpaved Road", "Unpaved Sidewalk",
    "Vegetation", "Wall", "Water leakage", "Water Pipes", "Wet surface", "Wheelchair", "White Cane", "Yard Waste"
]

# Specify the file path to save the objects
output_file_path = 'all_a11y_objects_new.csv'

# Open the file in write mode and save the objects in a comma followed by space-separated format
with open(output_file_path, 'w') as file:
    file.write(', '.join(['+' + obj for obj in objects]) + '\n')
    file.write(', '.join(['-' + obj for obj in objects]) + '\n')

print(f"Objects with signs have been saved to '{output_file_path}'")