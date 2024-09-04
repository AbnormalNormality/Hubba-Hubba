# Hubba Hubba

Hubba Hubba is a simple Tkinter application designed for quick access to your frequently used files. Easily launch your favorite files by creating and using a `.hub` file.

## Features

- Quick access to files via a simple UI.
- Keyboard shortcuts for easy file opening.
- Customizable file list through `.hub` files.

## How It Works

### Creating a Hub File

A `.hub` file is a plain text file listing the paths to the files you want to access quickly. Each file path should be on a new line.

**Example of a `.hub` file:**
```
C:\Program Files (x86)\Steam\steamapps\common\Skyrim Special Edition\skse64_loader.exe
C:\Users\user\Documents\important.txt
```

Ensure the file has the `.hub` extension.

### Setting Up Hubba Hubba

1. Double-click your `.hub` file.
2. When prompted to select a default app, scroll down and click "Choose another app."
3. Browse and select the `Hubba Hubba.exe` file.
4. Make sure to check "Always use this app to open .hub files" if you want Hubba Hubba to handle `.hub` files by default.

### Using Hubba Hubba

Once configured, you can open a `.hub` file anytime. Hubba Hubba will display buttons for each file listed in your hub file. Click a button to open the associated file.

## Code Overview

Here's a brief explanation of how the code works:

```python
from argparse import ArgumentParser

def load_hub(files):
    from AliasTkFunctions import fix_resolution_issue
    from tkinter import Tk, Button
    from os import startfile, chdir
    from os.path import basename, dirname

    fix_resolution_issue()

    main = Tk()
    main.bind("<FocusOut>", lambda _: main.destroy())
    main.overrideredirect(True)
    main.attributes("-topmost", True)

    main.configure(background="white")
    main.attributes("-transparentcolor", "white")

    keys = "1234567890"
    key_index = 0

    for file in files:
        button = Button(text=basename(file), command=lambda f=file: (chdir(dirname(f)), startfile(f), main.destroy()))
        button.pack(side="left", padx=(0 if key_index == 0 else 10, 0))

        if key_index < len(keys):
            main.bind(f"<KeyPress-{keys[key_index]}>", lambda _, b=button: (b.config(relief="sunken"),
                                                                            b.update_idletasks()))
            main.bind(f"<KeyRelease-{keys[key_index]}>", lambda _, b=button: (b.config(relief="raised"), b.invoke(),
                                                                              b.update_idletasks()))
            key_index += 1

    main.update_idletasks()
    window_width = main.winfo_reqwidth()
    window_height = main.winfo_reqheight()
    main.geometry(f"{window_width}x{window_height}+{(main.winfo_screenwidth() - window_width) // 2}+{
                     main.winfo_screenheight() - window_height - (main.winfo_screenheight() // 16)}")

    main.mainloop()

parser = ArgumentParser(description="Open a .hub file.")
parser.add_argument("file_path", type=str, nargs="?", help="Path to the .hub file")
file_path = parser.parse_args().file_path
if file_path:
    load_hub(open(file_path).read().splitlines())
```

- **`load_hub(files)`**: Loads the file paths from the `.hub` file and creates a simple UI with buttons for each file. Each button is bound to a specific key for quick access.
- **`ArgumentParser`**: Handles command-line arguments to specify the `.hub` file path.

## Additional Information
This information only applies to those using the Python code. You can ignore this part if you are using the executable file.

- **Dependencies**: Ensure you have the necessary libraries installed. Hubba Hubba relies on `tkinter` and `os`.
- **Customizing**: Feel free to modify the code to better suit your needs, such as changing the appearance of the buttons or adding additional functionality.

Enjoy using Hubba Hubba to streamline your file access!

<sub>**Thank you ChatGPT for helping me make this guide more understandable**</sub>
