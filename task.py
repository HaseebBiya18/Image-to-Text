import pytesseract
from PIL import Image
import cv2

def read_text_from_image(image_path, config="--psm 6 --oem 3"):
    try:
        img = cv2.imread(image_path)

        
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        pil_img = Image.fromarray(img_gray)

        text = pytesseract.image_to_string(pil_img, config=config)

        return text.strip()

    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None

# Example usage:
image_path = "download.jfif"
extracted_text = read_text_from_image(image_path)

if extracted_text:
    print("Extracted Text:")
    print(extracted_text)
else:
    print("Failed to extract text from the image.")
