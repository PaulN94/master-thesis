import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, root):
        # Question Generation
        self.qg_label = tk.Label(root, text="Question generation:")
        self.qg_label.grid(row=0, column=0, sticky="W")

        self.vpt_label = tk.Label(root, text="Variations per template:")
        self.vpt_label.grid(row=1, column=0, sticky="W")
        self.vpt_entry = tk.Entry(root)
        self.vpt_entry.grid(row=1, column=1)

        self.rpv_label = tk.Label(root, text="Reformulations per variation:")
        self.rpv_label.grid(row=2, column=0, sticky="W")
        self.rpv_entry = tk.Entry(root)
        self.rpv_entry.grid(row=2, column=1)

        self.epm_label = tk.Label(root, text="Experiments per model:")
        self.epm_label.grid(row=3, column=0, sticky="W")
        self.epm_entry = tk.Entry(root)
        self.epm_entry.grid(row=3, column=1)

        # LLM Evaluation
        self.llm_label = tk.Label(root, text="LLM evaluation:")
        self.llm_label.grid(row=4, column=0, sticky="W")

        self.llm_epm_label = tk.Label(root, text="Experiments per model:")
        self.llm_epm_label.grid(row=5, column=0, sticky="W")
        self.llm_epm_entry = tk.Entry(root)
        self.llm_epm_entry.grid(row=5, column=1)

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit", command=self.submit)
        self.submit_button.grid(row=6, column=0, columnspan=2, pady=(20, 0))  # Added space above this button

    def submit(self):
        vpt = self.vpt_entry.get()
        rpv = self.rpv_entry.get()
        epm = self.epm_entry.get()
        llm_epm = self.llm_epm_entry.get()

        msg = f"Variations per Template: {vpt}\nReformulations per Variation: {rpv}\nExperiments per Model (QG): {epm}\nExperiments per Model (LLM): {llm_epm}"
        messagebox.showinfo("Input Values", msg)

root = tk.Tk()
app = App(root)
root.mainloop()
