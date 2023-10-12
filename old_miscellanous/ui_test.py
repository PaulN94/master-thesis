import tkinter as tk
from tkinter import ttk

def save_settings():
    username = entry_username.get()
    color = combo_color.get()
    # Save the settings (just print them here as an example)
    print(f"Saved settings:\nUsername: {username}\nColor: {color}")

# Create the main window
root = tk.Tk()
root.title("Settings")

# Create and place the widgets
tk.Label(root, text="Username:").grid(column=0, row=0, padx=10, pady=10, sticky="w")
entry_username = tk.Entry(root)
entry_username.grid(column=1, row=0, padx=10, pady=10)

tk.Label(root, text="Favorite Color:").grid(column=0, row=1, padx=10, pady=10, sticky="w")
combo_color = ttk.Combobox(root, values=["Red", "Green", "Blue"])
combo_color.grid(column=1, row=1, padx=10, pady=10)

tk.Button(root, text="Save Settings", command=save_settings).grid(column=0, row=2, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
