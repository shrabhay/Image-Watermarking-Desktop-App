from tkinter import *
from tkinter import filedialog, messagebox, ttk

from PIL import Image, ImageTk, ImageDraw, ImageFont
import os

FONT_TYPES = ('Allura', 'Barlow', 'Caveat', 'Inter', 'Kaushan_Script', 'Lato', 'Libre_Baskerville', 'Merriweather',
              'Mona_Sans', 'Montserrat', 'Noto_Sans', 'Nunito', 'Open_Sans', 'Outfit', 'Parkinsans',
              'Playfair_Display', 'Playwrite_HR_Lijeva', 'Poppins', 'Quicksand', 'Raleway', 'Roboto', 'Rubik',
              'Sacramento', 'Tangerine')

FONT_COLORS = ('AliceBlue', 'AntiqueWhite', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque', 'Black',
               'BlanchedAlmond', 'Blue', 'BlueViolet', 'Brown', 'Burlywood', 'CadetBlue', 'Chartreuse', 'Chocolate',
               'Coral', 'CornflowerBlue', 'Cornsilk', 'Crimson', 'Cyan', 'DarkBlue', 'DarkCyan', 'DarkGoldenRod',
               'DarkGray', 'DarkGreen', 'DarkKhaki', 'DarkMagenta', 'DarkOliveGreen', 'DarkOrange', 'DarkOrchid',
               'DarkRed', 'DarkSalmon', 'DarkSeaGreen', 'DarkSlateBlue', 'DarkSlateGray', 'DarkTurquoise',
               'DarkViolet', 'DeepPink', 'DeepSkyBlue', 'DimGray', 'DodgerBlue', 'FireBrick', 'FloralWhite',
               'ForestGreen', 'Fuchsia', 'Gainsboro', 'GhostWhite', 'Gold', 'GoldenRod', 'Gray', 'Green',
               'GreenYellow', 'HoneyDew', 'HotPink', 'IndianRed', 'Indigo', 'Ivory', 'Khaki', 'Lavender',
               'LavenderBlush', 'LawnGreen', 'LemonChiffon', 'LightBlue', 'LightCoral', 'LightCyan',
               'LightGoldenRodYellow', 'LightGray', 'LightGreen', 'LightPink', 'LightSalmon', 'LightSeaGreen',
               'LightSkyBlue', 'LightSlateGray', 'LightSteelBlue', 'LightYellow', 'Lime', 'LimeGreen', 'Linen',
               'Magenta', 'Maroon', 'MediumAquaMarine', 'MediumBlue', 'MediumOrchid', 'MediumPurple',
               'MediumSeaGreen', 'MediumSlateBlue', 'MediumSpringGreen', 'MediumTurquoise', 'MediumVioletRed',
               'MidnightBlue', 'MintCream', 'MistyRose', 'Moccasin', 'NavajoWhite', 'Navy', 'OldLace', 'Olive',
               'OliveDrab', 'Orange', 'OrangeRed', 'Orchid')

FONT_SIZES = (10, 12, 14, 16, 18, 20, 22, 24, 30, 36, 48, 64, 70, 80, 100, 120, 150, 200)

WATERMARK_PLACEMENTS = ('Top_Left', 'Top_Right', 'Center', 'Bottom_Left', 'Bottom_Right', 'Custom')


class Watermarker:
    def __init__(self, root):
        self.root = root
        self.root.title('Image Watermarking Desktop App')
        self.root.geometry('600x700')

        # Variables
        self.image_path = None
        self.watermarked_image = None
        self.watermark_text = StringVar()
        self.selected_font = StringVar(value='Allura')
        self.selected_color = StringVar(value='Black')
        self.selected_size = IntVar(value=20)
        self.selected_position = StringVar(value='Center')
        self.custom_x = IntVar(value=0)
        self.custom_y = IntVar(value=0)

        # Widgets
        self.upload_button = None
        self.image_label = None
        self.watermark_label = None
        self.watermark_entry = None
        self.font_type = None
        self.font_color = None
        self.font_size = None
        self.watermark_placement = None
        self.custom_x_label = None
        self.custom_x_entry = None
        self.custom_y_label = None
        self.custom_y_entry = None
        self.add_watermark_button = None
        self.save_button = None

        # Fonts Directory
        self.font_dir = 'Fonts'

        # GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Upload Image Button
        self.upload_button = Button(self.root, text='Upload Image', command=self.upload_image)
        self.upload_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Image Preview
        self.image_label = Label(self.root, text='No Image Uploaded')
        self.image_label.grid(row=1, column=0, columnspan=2, rowspan=8, padx=10, pady=10)

        # Watermark Text Input
        self.watermark_label = Label(self.root, text='Watermark Text: ')
        self.watermark_label.grid(row=1, column=2, sticky='w', padx=10, pady=10)
        self.watermark_entry = Entry(self.root, textvariable=self.watermark_text)
        self.watermark_entry.grid(row=1, column=3, columnspan=2, sticky='ew', padx=10, pady=5)

        # Font Type Dropdown
        self.font_type = Label(self.root, text='Font: ')
        self.font_type.grid(row=2, column=2, sticky='w', padx=10, pady=10)
        font_dropdown = ttk.Combobox(self.root, textvariable=self.selected_font)
        font_dropdown['values'] = FONT_TYPES
        font_dropdown.grid(row=2, column=3, columnspan=2, sticky='ew', padx=10, pady=5)

        # Font Color Dropdown
        self.font_color = Label(self.root, text='Font Color: ')
        self.font_color.grid(row=3, column=2, sticky='w', padx=10, pady=10)
        color_dropdown = ttk.Combobox(self.root, textvariable=self.selected_color)
        color_dropdown['values'] = FONT_COLORS
        color_dropdown.grid(row=3, column=3, columnspan=2, sticky='ew', padx=10, pady=5)

        # Font Size Dropdown
        self.font_size = Label(self.root, text='Font Size: ')
        self.font_size.grid(row=4, column=2, sticky='w', padx=10, pady=10)
        size_dropdown = ttk.Combobox(self.root, textvariable=self.selected_size)
        size_dropdown['values'] = FONT_SIZES
        size_dropdown.grid(row=4, column=3, columnspan=2, sticky='ew', padx=10, pady=5)

        # Watermark Placement Dropdown
        self.watermark_placement = Label(self.root, text='Watermark Position: ')
        self.watermark_placement.grid(row=5, column=2, sticky='w', padx=10, pady=10)
        position_dropdown = ttk.Combobox(self.root, textvariable=self.selected_position)
        position_dropdown['values'] = WATERMARK_PLACEMENTS
        position_dropdown.grid(row=5, column=3, columnspan=2, sticky='ew', padx=10, pady=5)
        position_dropdown.bind('<<ComboboxSelected>>', self.toggle_custom_position_fields)

        # Custom Watermark Placement Inputs
        self.custom_x_label = Label(self.root, text='Custom X: ')
        self.custom_x_label.grid(row=6, column=2, sticky='w', padx=10, pady=10)
        self.custom_x_entry = Entry(self.root, textvariable=self.custom_x)
        self.custom_x_entry.grid(row=6, column=3, sticky='ew', padx=10, pady=2)

        self.custom_y_label = Label(self.root, text='Custom Y: ')
        self.custom_y_label.grid(row=7, column=2, sticky='w', padx=10, pady=10)
        self.custom_y_entry = Entry(self.root, textvariable=self.custom_y)
        self.custom_y_entry.grid(row=7, column=3, sticky='ew', padx=10, pady=2)

        # Add Watermark Button
        self.add_watermark_button = Button(self.root, text='Add Watermark', command=self.add_watermark)
        self.add_watermark_button.grid(row=8, column=2, columnspan=2, padx=10, pady=10)

        # Save Image Button
        self.save_button = Button(self.root, text='Save Image', command=self.save_image)
        self.save_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

        # Configure Column Weights for Resizing
        self.root.columnconfigure(1, weight=1)

    def toggle_custom_position_fields(self, event=None):
        if self.selected_position.get() == 'Custom':
            self.custom_x_entry.config(state='normal')
            self.custom_y_entry.config(state='normal')
        else:
            self.custom_x_entry.config(state='disabled')
            self.custom_y_entry.config(state='disabled')

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.png; *.jpg; *.jpeg; *.svg; *.webp')])
        if file_path:
            self.image_path = file_path
            img = Image.open(self.image_path)

            self.resize_window_to_image(img)

            img.thumbnail((500, 500))
            img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=img_tk, text='')
            self.image_label.image = img_tk

    def resize_window_to_image(self, image):
        img_width, img_height = image.size
        new_width = img_width
        new_height = img_height
        self.root.geometry(f'{new_width}x{new_height}')

    def add_watermark(self):
        if not self.image_path:
            messagebox.showerror('Error', 'Please upload an image first!')

        img = Image.open(self.image_path)
        draw = ImageDraw.Draw(img)

        # Font Settings
        selected_font = self.selected_font.get()
        font_path = os.path.join(self.font_dir, selected_font, f'{selected_font.lower()}.ttf')
        try:
            font = ImageFont.truetype(font_path, self.selected_size.get())
        except IOError:
            messagebox.showerror('Error', f'Font file for {selected_font} not found!')
            return

        # Text Placement
        text = self.watermark_text.get()
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        selected_position = self.selected_position.get()
        if selected_position == 'Top_Left':
            x, y = 10, 10
        elif selected_position == 'Top_Right':
            x, y = img.width - text_width - 10, 10
        elif selected_position == 'Center':
            x, y = (img.width - text_width) // 2, (img.height - text_height) // 2
        elif selected_position == 'Bottom_Left':
            x, y = 10, img.height - text_height - 10
        elif selected_position == 'Bottom_Right':
            x, y = img.width - text_width - 10, img.height - text_height - 10
        else:
            x, y = self.custom_x.get(), self.custom_y.get()

        # Font Color
        color = self.selected_color.get().lower()

        # Draw Text
        draw.text((x, y), text, font=font, fill=color)
        self.watermarked_image = img

        # Update Preview
        img.thumbnail((500, 500))
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

    def save_image(self):
        if not self.watermarked_image:
            messagebox.showerror('Error', 'No watermarked image to save!')
            return

        file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[('JPG Files', '*.jpg')])
        if file_path:
            self.watermarked_image.save(file_path)
            messagebox.showinfo('Success', 'Image saved successfully!!')
