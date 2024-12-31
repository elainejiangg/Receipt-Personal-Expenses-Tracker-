import pytesseract
from PIL import Image

# Specify the path to the Tesseract executable (if not in your system's PATH)
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract' 

# Open the image file
image = Image.open('testRecipt.png') 

# Extract text from the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)