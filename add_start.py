import os
import tkinter
import tkinter.filedialog


def add_start(file):
    """Adds a file to the Windows startup folder"""

    start_dir = os.path.expandvars("%APPDATA%") + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    print(start_dir)

    in_file_path = start_dir + "\\" + os.path.basename(file)
    if not os.path.exists(in_file_path):
        os.symlink(file, in_file_path)
        print(f"File {file} added to startup")
    else:
        print(f"File {file} already exists in startup")


if __name__ == "__main__":
    tk = tkinter.Tk()
    tk.title("Add to startup")
    # Set the window background color to black
    tk.configure(background="#206de3")
    # Set the window size to 300x200 pixels
    tk.geometry("300x200")

    # Create a label widget
    label = tkinter.Label(tk, text="Add File To Start Menu", font=("Arial", 12), bg="#206de3", fg="white")
    # Add the label to the window
    label.pack(pady=10)

    # Create a button widget
    button = tkinter.Button(tk, text="Select File", command=lambda: add_start(tkinter.filedialog.askopenfilename()))
    # Add the button to the window
    button.pack(pady=10)

    button2 = tkinter.Button(tk, text="Open Folder", command=lambda: os.startfile(os.path.expandvars("%APPDATA%") + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"))
    # Add the button to the window
    button2.pack(pady=10)
    # Run the main loop
    tk.mainloop()

    # This code is a modified version of the code found at https://github.com/xietongrui/add-startup
