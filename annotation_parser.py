import os

# ------------------------------
# Load annotation file
# ------------------------------
def load_annotations(annotation_path):
    annotations = {}

    if not os.path.exists(annotation_path):
        print("Annotation file not found!")
        return annotations

    with open(annotation_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        parts = line.strip().split()

        # First part is image name
        image_name = parts[0]

        boxes = []

        # Remaining parts are bounding boxes
        for box_data in parts[1:]:
            values = box_data.split(",")

            if len(values) == 5:
                x1, y1, x2, y2, class_id = values

                boxes.append((
                    int(x1),
                    int(y1),
                    int(x2),
                    int(y2),
                    int(class_id)
                ))

        annotations[image_name] = boxes

    return annotations


# ------------------------------
# Load class names
# ------------------------------
def load_classes(classes_path):
    classes = {}

    if not os.path.exists(classes_path):
        print("Classes file not found!")
        return classes

    with open(classes_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for idx, line in enumerate(lines):
        classes[idx] = line.strip()

    return classes


# ------------------------------
# Test the functions
# ------------------------------
if __name__ == "__main__":

    annotation_file = "dataset/_annotations.txt"
    classes_file = "dataset/_classes.txt"

    annotations = load_annotations(annotation_file)
    classes = load_classes(classes_file)

    print("\nClass Mapping:")
    print(classes)

    print("\nFirst Image Annotation:")
    for key, value in annotations.items():
        print("Image:", key)
        print("Boxes:", value)
        break
