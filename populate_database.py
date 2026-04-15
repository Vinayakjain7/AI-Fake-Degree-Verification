import os
from ocr_module import extract_raw_fields
from database import create_database, insert_certificate

DATASET_FOLDER = "dataset/clean"


def populate_database():

    create_database()

    count = 0

    for filename in os.listdir(DATASET_FOLDER):

        if filename.lower().endswith((".jpg", ".png")):

            image_path = os.path.join(DATASET_FOLDER, filename)

            print(f"Processing: {filename}")

            raw_data = extract_raw_fields(image_path)

            if raw_data is None:
                print("Skipped:", filename)
                continue

            if all(key in raw_data for key in ["Student Name", "Course", "University", "Issue Date"]):

                insert_certificate(
                    filename,
                    raw_data["Student Name"],
                    raw_data["Course"],
                    raw_data["University"],
                    raw_data["Issue Date"]
    )

                count += 1
                print("Inserted:", filename)

    print(f"\nDatabase populated with {count} clean certificates.")


if __name__ == "__main__":
    populate_database()