import tkinter as tk
from tkinter import ttk, messagebox


class IntegratedApp(tk.Tk):
    def __init__(self, data):
        super().__init__()

        self.data = data
        self.title("Experiment Selection and Configuration")
        self.geometry("600x800")

        # Configuration Section
        self.config_label = tk.Label(self, text="Configuration:")
        self.config_label.pack()

        self.vpt_label = tk.Label(self, text="Variations per template:")
        self.vpt_label.pack()
        self.vpt_entry = tk.Entry(self)
        self.vpt_entry.pack()

        self.rpv_label = tk.Label(self, text="Reformulations per variation:")
        self.rpv_label.pack()
        self.rpv_entry = tk.Entry(self)
        self.rpv_entry.pack()

        self.epm_label = tk.Label(self, text="Experiments per model:")
        self.epm_label.pack()
        self.epm_entry = tk.Entry(self)
        self.epm_entry.pack()

        self.submit_button = tk.Button(
            self, text="Submit Configuration", command=self.submit_config)
        self.submit_button.pack(pady=(20, 0))

        # Selection Section
        self.tree = ttk.Treeview(
            self, columns=('check',), height=len(self.data))
        self.tree.column('check', width=50)
        self.tree.heading('#0', text='Options')
        self.tree.heading('check', text='Select')
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Populate the tree with data
        for llm in self.data["llms"]:
            llm_id = self.tree.insert(
                '', 'end', text=self.data["llms"][llm], values=(''))
            for model in self.data["optimization models"]:
                model_id = self.tree.insert(
                    llm_id, 'end', text=self.data["optimization models"][model], values=(''))
                for task in self.data["tasks"]:
                    task_id = self.tree.insert(
                        model_id, 'end', text=self.data["tasks"][task], values=(''))
                    for dist in self.data["distribution"]:
                        dist_id = self.tree.insert(
                            task_id, 'end', text=self.data["distribution"][dist], values=(''))
                        for icl in self.data["ICL"]:
                            self.tree.insert(
                                dist_id, 'end', text=self.data["ICL"][icl], values=(''))

        self.tree.bind('<ButtonRelease-1>', self.check_child)

        # Adding Select All and Unselect All buttons
        self.select_all_button = tk.Button(
            self, text="Select All", command=self.select_all)
        self.select_all_button.pack()
        self.unselect_all_button = tk.Button(
            self, text="Unselect All", command=self.unselect_all)
        self.unselect_all_button.pack()

    def submit_config(self):
        vpt = self.vpt_entry.get()
        rpv = self.rpv_entry.get()
        epm = self.epm_entry.get()

        msg = f"Variations per Template: {vpt}\nReformulations per Variation: {rpv}\nExperiments per Model (QG): {epm}"
        messagebox.showinfo("Input Values", msg)

    def select_all(self):
        for item in self.tree.get_children(''):
            self.tree.set(item, 'check', '✔')
            self.update_children(item, '✔')

    def unselect_all(self):
        for item in self.tree.get_children(''):
            self.tree.set(item, 'check', '')
            self.update_children(item, '')

    def update_children(self, item, value):
        children = self.tree.get_children(item)
        for child in children:
            self.tree.set(child, 'check', value)
            self.update_children(child, value)

    def check_child(self, event):
        col = self.tree.identify_column(event.x)
        row_id = self.tree.identify_row(event.y)
        item = self.tree.selection()

        if row_id and col == '#1':
            check = '✔' if self.tree.set(item, 'check') == '' else ''
            self.tree.set(item, 'check', check)
            self.check_parent(item, check)

    def check_parent(self, item, check):
        parent = self.tree.parent(item)
        if parent:
            if check == '':
                all_siblings_unchecked = all(
                    self.tree.set(sibling, 'check') == ''
                    for sibling in self.tree.get_children(parent)
                )
                if all_siblings_unchecked:
                    self.tree.set(parent, 'check', check)
            else:
                self.tree.set(parent, 'check', check)
            self.check_parent(parent, check)


# The data dictionary and initialization remain the same as your provided code.
data = {
    "llms": {
        "1": "LLM1: GPT-3.5-turbo",
        "2": "LLM2: GPT-4"
    },
    "optimization models": {
        "1": "Model1: Knapsack",
        "2": "Model2: MMNL",
        "3": "Model3: CAP"
    },
    "tasks": {
        "1": "Task1: Build",
        "2": "Task2: Transform"
    },
    "distribution": {
        "0": "Dist0: Out-of-distribution_ICL",
        "1": "Dist1: In-distribution_ICL"
    },
    "ICL": {
        "0": "ICL0: Zero-shot",
        "1": "ICL1: One-shot",
        "2": "ICL2: Two-shot",
        "3": "ICL3: Three-shot",
        "4": "ICL4: Four-shot",
        "5": "ICL5: Five-shot",
        "6": "ICL6: Six-shot",
        "7": "ICL7: Seven-shot",
        "8": "ICL8: Eight-shot",
        "9": "ICL9: Nine-shot",
        "10": "ICL10: Ten-shot"
    }
}

app = IntegratedApp(data)
app.mainloop()
