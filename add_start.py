import os
import tkinter
import tkinter.filedialog
from tkinter import messagebox


if __name__ == "__main__":
    tk = tkinter.Tk()
    tk.title("Add to startup")
    # Set the window background color to black
    tk.configure(background="#206de3")
    # Set the window size to 300x200 pixels
    tk.geometry("300x200")

    path = tkinter.BooleanVar()
    path.set(False)

    def is_just_for_me():
        if path.get():
            return os.path.expandvars("%APPDATA%")
        else:
            return os.path.expandvars("%PROGRAMDATA%")


    def add_start(file):
        """Adds a file to the Windows startup folder"""

        start_dir = is_just_for_me() + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
        print(start_dir)

        in_file_path = start_dir + "\\" + os.path.basename(file)
        if not os.path.exists(in_file_path):
            os.symlink(file, in_file_path)
            messagebox.showinfo("Success", f"File {file} added to startup")
        else:
            messagebox.showerror("Error", f"File {file} already exists in startup")

    # Create a label widget
    label = tkinter.Label(tk, text="Add File To Start Menu", font=("Arial", 12), bg="#206de3", fg="white")
    # Add the label to the window
    label.pack(pady=10)

    # Create a checkbox widget
    checkbox = tkinter.Checkbutton(tk, text="Is Just For Me", font=("Arial", 12), variable=path)
    checkbox.pack(pady=10)

    # Create a button widget
    button = tkinter.Button(tk, text="Select File", command=lambda: add_start(tkinter.filedialog.askopenfilename()))
    # Add the button to the window
    button.pack(pady=10)

    button2 = tkinter.Button(tk, text="Open Folder", command=lambda: os.startfile(is_just_for_me() + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"))
    # Add the button to the window
    button2.pack(pady=10)
    # Run the main loop
    tk.mainloop()

    # This code is a modified version of the code found at https://github.com/xietongrui/Add-Start-Menu
