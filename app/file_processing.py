from PIL import Image
import io
import csv
import os


def process_image(file: bytes, output_path: str) -> str:
    # Ensure the directory for output_path exists
    directory = os.path.dirname(output_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Open image and process (resize example)
    image = Image.open(io.BytesIO(file))
    image = image.resize((300, 300))  # Resize the image to 300x300
    image.save(output_path)

    return output_path


def process_csv(file: bytes) -> list:
    # Parse the CSV file and return data as list of dicts
    decoded_file = file.decode('utf-8')
    csv_reader = csv.DictReader(decoded_file.splitlines())
    return [row for row in csv_reader]
