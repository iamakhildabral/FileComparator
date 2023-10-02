import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from turtle import st

# main window
root = tk.Tk()
root.title("File Comparator Service")
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
        download_label.config(
            text=f"File saved to: {save_path}")

# Function to show a confirmation dialog when the COMPARE button is clicked


def confirm_compare():
    result = messagebox.askyesno(
        "Confirmation", "Do you really want to compare the files?")
    if result:
        # You can replace this with your comparison logic
        print("Comparing files...")


# creating label for MFOL and LEGACY files
mfol_label = tk.Label(root, text="MFOL File :")
legacy_label = tk.Label(root, text="LEGACY File :")
compare_file = tk.Label(root, text="Click to Compare Files :")
result_label = tk.Label(
    root, text="STATUS : Not compared Yet", relief="solid", bd=1)
download_label = tk.Label(root, text="Download Results")

# Create buttons for selecting files and downloading
mfol_button = tk.Button(root, text="Browse",
                        command=lambda: browse_file(mfol_label))
legacy_button = tk.Button(
    root, text="Browse", command=lambda: browse_file(legacy_label))
# Call confirm_compare function
compare_button = tk.Button(
    root, text="COMPARE", command=confirm_compare)
download_button = tk.Button(root, text="Download", command=download_file)

# Arrange widgets using the grid layout
mfol_label.grid(row=0,      column=0, padx=50, pady=10, sticky="w")
legacy_label.grid(row=1,    column=0, padx=50, pady=10, sticky="w")
compare_file.grid(row=2,    column=0, padx=50, pady=10, sticky="w")
result_label.grid(row=3,    column=0, padx=50, pady=10, sticky="w")
download_label.grid(row=4,  column=0, padx=50, pady=10, sticky="w")

mfol_button.grid(row=0,     column=1, padx=50, pady=10, columnspan=2)
legacy_button.grid(row=1,   column=1, padx=50, pady=10, columnspan=2)
compare_button.grid(row=2,  column=1, padx=50, pady=10, columnspan=2)
download_button.grid(row=4, column=1, padx=50, pady=10, columnspan=2)

result_label.grid(row=3, padx=50, pady=10, sticky="nsew", columnspan=4)

# mainloop
root.mainloop()
