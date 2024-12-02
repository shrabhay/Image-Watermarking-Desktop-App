# Image Watermarking Desktop App
## Description
This project provides a user-friendly GUI application for adding text watermarks to images. It supports customizable font types, sizes, colors, and positions, including a custom placement option.

---

## Features
* Upload images in various formats (PNG, JPG, JPEG, SVG, WEBP).
* Apply text watermarks with customizable fonts, colors, sizes, and placements.
* Preview watermarked images before saving.
* Save watermarked images in JPG format.

---

## Getting Started
### Prerequisites
Ensure the following are installed on your system:

* Python 3.8 or later
* Required Python libraries (`Pillow`, `tkinter`)

### Installation
1. Clone the repository:
    ```commandline
    git clone https://github.com/shrabhay/Image-Watermarking-Desktop-App
    cd Image-Watermarking-Desktop-App
    ```

2. Install dependencies:
    ```commandline
    pip install PIL
    pip install tkinter
    ```

3. Ensure the `Fonts` directory contains the font files matching the names in the `FONT_TYPES` list (e.g., `allura.ttf`, `barlow.ttf`).

---

## Running the Application
Start the application by running the following command:
    ```commandline
    python image_watermarking_app.py
    ```

---

## Using the Application
1. **Upload an Image**: Click the "Upload Image" button and select an image file.
2. **Enter Watermark Text**: Input your desired watermark text in the provided field.
3. **Customize Watermark**:
   * **Font**: Choose a font type from the dropdown.
   * **Font Color**: Select a color from the list.
   * **Font Size**: Adjust the text size as needed.
   * **Position**: Set the watermark position or choose "Custom" to specify exact coordinates.
4. **Preview**: The preview updates with the applied watermark.
5. Save Image: Click "Save Image" to save the watermarked image.

---

## Customizing Fonts
To use different fonts, follow these steps:

1. **Add Font Files**: Place the `.ttf` files of the desired fonts in the Fonts directory.
2. **Update Font List**:
   * Edit the `FONT_TYPES` list in `watermarker.py` to include the new font names.
   * Ensure each name matches the corresponding `.ttf` file (e.g., for `CustomFont`, add `CustomFont` to `FONT_TYPES` and place `customfont.ttf` in `Fonts`).

---

## Project Structure
```commandline
image-watermarking-app/
│
├── image_watermarking_app.py     # Main application entry point
├── watermarker.py                # Watermarking logic and GUI components
├── Fonts/                        # Directory containing .ttf font files
```

---

## License
This project is licensed under the MIT License.

Feel free to reach out if you encounter issues or have suggestions for improvement!
