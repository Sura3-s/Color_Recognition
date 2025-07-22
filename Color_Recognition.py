import cv2
import numpy as np

# Function to identify the name of a color based on BGR values
def identify_color(bgr_color):
    colors = {
        'Red': (0, 0, 255),
        'Green': (0, 255, 0),
        'Blue': (255, 0, 0),
        'Yellow': (0, 255, 255),
        'Black': (0, 0, 0)
    }
    for color_name, bgr_val in colors.items():
        if np.allclose(bgr_color, bgr_val, atol=40):
            return color_name
    return 'Unknown'

# Load the image
image = cv2.imread('Color_Image.png')
if image is None:
    print("Image not found.")
    exit()

# Make a copy of the image to draw on
updated_image = image.copy()

# Mouse click callback
def mouse_callback(event, x, y, flags, param):
    global updated_image
    if event == cv2.EVENT_LBUTTONDOWN:
        bgr_color = image[y, x]
        color_name = identify_color(bgr_color)
        print(f"Position ({x},{y}) - BGR: {bgr_color} - Color: {color_name}")

        # Draw a filled rectangle for text background
        rectangle_start = (10, 10)
        rectangle_end = (200, 40)
        cv2.rectangle(updated_image, rectangle_start, rectangle_end, (255, 255, 255), -1)

        # Put the color name text
        cv2.putText(updated_image, f"Color: {color_name}", (15, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

# Set the callback
cv2.namedWindow('Color Recognition')
cv2.setMouseCallback('Color Recognition', mouse_callback)

# Show image in a loop
while True:
    cv2.imshow('Color Recognition', updated_image)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Press 'q' to quit
        break

cv2.destroyAllWindows()