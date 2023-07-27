import tkinter as tk
from tkinter import filedialog
from PIL import Image


from asgn_8 import manipulator, exif_extractor

def add_overlay_clicked():
    if selected_image_path:
        manipulator.manipulate(selected_image_path[0])
        render_image("manipulated_image.png")
    else:
        show_popup("Please select an image first!")


def exif_extract_clicked():
    if selected_image_path:
        # show_popup("Action successful! exif_extract was clicked with image: " + str(selected_image_path))
        exif_extractor.extract_exif_data(selected_image_path[0])
    else:
        show_popup("Please select an image first!")


def browse_image():
    global selected_image_path
    selected_image_path = filedialog.askopenfilenames(filetypes=[('Images', '*.jpg *.jpeg *.png')])


def center_window(root, width, height):
    # Calculate the x and y coordinates to center the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")


def show_popup(message, duration=2000):
    popup = tk.Toplevel(root)
    popup.title("Popup")
    popup.geometry("250x100")
    center_window(popup, 250, 100)
    popup_label = tk.Label(popup, text=message)
    popup_label.pack(pady=20)
    root.after(duration, popup.destroy)


def render_image(image_path):
    img = Image.open(image_path)
    img.show()


# Create the main application window
root = tk.Tk()
root.title("Button App")

# Set the window size (width, height)
window_width = 500
window_height = 400

# Center the window on the screen
center_window(root, window_width, window_height)

# Create a button to browse and select an image
browse_button = tk.Button(root, text="Browse Image", command=browse_image)
browse_button.pack(pady=10)

# Create two buttons
button1 = tk.Button(root, text="Add red overlay", command=add_overlay_clicked)
button1.pack(pady=10)

button2 = tk.Button(root, text="Extract Exif", command=exif_extract_clicked)
button2.pack(pady=10)

# Create a label to display messages
label = tk.Label(root, text="Click a button after selecting an image!")
label.pack(pady=20)

# Create a label to display the rendered image
image_tk = None
image_label = tk.Label(root, image=image_tk)
image_label.pack()

# Variable to store the path of the selected image
selected_image_path = None

# Start the main event loop
root.mainloop()
