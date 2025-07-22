# Color Recognition with OpenCV 🎨

## Project Description :
This project is a simple color recognition program created using **Python** and the **OpenCV** library.  
It allows the user to click on any point in the image to identify the color at that pixel.

Once you click on the image :
- The program prints the **coordinates**, **BGR values**, and **color name** in the terminal.
- The name of the color also appears at the **top of the image** inside a white rectangle for clear visibility.

---

## Requirements
- Python 
- OpenCV
- Numpy

### Install required libraries :
```
pip install opencv-python
pip install numpy
```

---

## How to Run the Project ?
1. Make sure the image is saved with the name :
```
Color_Image.png
```
and placed in the same folder as the Python code file.

2. Run the code in the terminal :
```
python color_recognition.py
```

3. A window with the image will open.

4. Click anywhere in the image
- The terminal will show :
```
Position (x,y) - BGR: [B G R] - Color: ColorName
```
- The top of the image will display the name of the selected color.

5. To exit, press the '**q**' key.

---

## Supported Colors 
The program currently recognizes the following colors : 
- Red
- Green
- Blue
- Yellow
- Black

You can add more colors by editing the `identify_color` function inside the code.

---

## Example of Output :
If you click on a green area :
```
Position (120, 45) - BGR: [  0 255   0] - Color: Green
```
And the image will show "Color: Green" at the top.

---

## Notes
- Ensure the image file name is exactly **Color_Image.png**.
- You can enhance the project by adding more colors or saving the output image.

---

## Author :
Made By: **Sura Abdullah Alkhuzaim**
