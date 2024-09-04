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
