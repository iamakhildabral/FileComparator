import tkinter as tk
from tkinter import filedialog

# main window
root = tk.Tk()
root.title("File Comparator Service ")
root.geometry("500x500")

# Function to open a file dialog and update the label text


def browse_file(label):
    file_path = filedialog.askopenfilename()
    label.config(text=file_path)

# Function for the file download action (you can customize this)


def download_file():
    # Replace this with your file download logic
    # For simplicity, I'm just displaying a message here
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[
                                             ("Text Files", "*.txt"), ("All Files", "*.*")])
    if save_path:
        comparator_file_download_label.config(
            text=f"File saved to: {save_path}")


# creating lable for mfol and legacy files
mfol_label = tk.Label(root, text="MFOL File")
legacy_label = tk.Label(root, text="LEGACY File")

comparator_file_download_label = tk.Label(root, text="Download Results")

# Create buttons for selecting files and downloading
mfol_button = tk.Button(root, text="Browse",
                        command=lambda: browse_file(mfol_label))
legacy_button = tk.Button(
    root, text="Browse", command=lambda: browse_file(legacy_label))
download_button = tk.Button(root, text="Download", command=download_file)

# Arrange widgets using the grid layout
mfol_label.grid(row=0, column=0)
legacy_label.grid(row=1, column=0)
comparator_file_download_label.grid(row=2, column=1)
mfol_button.grid(row=0, column=1)
legacy_button.grid(row=1, column=1)
download_button.grid(row=2, column=0)

# mainloop
root.mainloop()
