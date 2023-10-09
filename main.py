import tkinter as tk
from tkinter import ttk, messagebox, font  # Importing font

class IntegratedApp(tk.Tk):
    def __init__(self, data):
        super().__init__()

        self.title_font = font.Font(family="Helvetica", size=14, underline=1)  # Creating a font object

        self.data = data
        self.title("Experiment Selection and Configuration")
        self.geometry("800x800")

        # Main frame
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left frame inside the main frame
        left_frame = tk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Experiment Name Section in Left Frame
        self.experiment_name_label = tk.Label(left_frame, text="Experiment name:", font=self.title_font)
        self.experiment_name_label.pack(pady=(10, 5))
        self.experiment_name_entry = tk.Entry(left_frame)
        self.experiment_name_entry.pack(pady=(0, 20))

        # Question Generation Section
        self.config_label = tk.Label(left_frame, text="Question generation:", font=self.title_font)
        self.config_label.pack()
        self.vpt_label = tk.Label(left_frame, text="Variations per template:")
        self.vpt_label.pack()
        self.vpt_entry = tk.Entry(left_frame)
        self.vpt_entry.pack()
        self.rpv_label = tk.Label(left_frame, text="Reformulations per variation:")
        self.rpv_label.pack()
        self.rpv_entry = tk.Entry(left_frame)
        self.rpv_entry.pack()
        self.epm_label = tk.Label(left_frame, text="Experiments per model:")
        self.epm_label.pack()
        self.epm_entry = tk.Entry(left_frame)
        self.epm_entry.pack()
        self.llm_temp_label = tk.Label(left_frame, text="LLM temperature at reformulating:")
        self.llm_temp_label.pack(pady=(10, 5))
        self.llm_temp_entry = tk.Entry(left_frame)
        self.llm_temp_entry.pack(pady=(0, 20))

        # LLM Evaluation Section
        self.llm_label = tk.Label(left_frame, text="LLM evaluation:", font=self.title_font)
        self.llm_label.pack()
        self.llm_epm_label = tk.Label(left_frame, text="Experiments per model:")
        self.llm_epm_label.pack()
        self.llm_epm_entry = tk.Entry(left_frame)
        self.llm_epm_entry.pack()

        # Selection Section
        self.tree = ttk.Treeview(left_frame, columns=('check',), height=len(self.data))
        self.tree.column('check', width=50)
        self.tree.heading('#0', text='Options')
        self.tree.heading('check', text='Select')
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Populate the tree with data
        for llm in self.data["llms"]:
            llm_id = self.tree.insert('', 'end', text=self.data["llms"][llm], values=(''))
            for model in self.data["optimization models"]:
                model_id = self.tree.insert(llm_id, 'end', text=self.data["optimization models"][model], values=(''))
                for task in self.data["tasks"]:
                    task_id = self.tree.insert(model_id, 'end', text=self.data["tasks"][task], values=(''))
                    for dist in self.data["distribution"]:
                        dist_id = self.tree.insert(task_id, 'end', text=self.data["distribution"][dist], values=(''))
                        for icl in self.data["ICL"]:
                            self.tree.insert(dist_id, 'end', text=self.data["ICL"][icl], values=(''))

        self.tree.bind('<ButtonRelease-1>', self.check_child)

        # Adding Select All and Unselect All buttons
        self.select_all_button = tk.Button(left_frame, text="Select All", command=self.select_all)
        self.select_all_button.pack()
        self.unselect_all_button = tk.Button(left_frame, text="Unselect All", command=self.unselect_all)
        self.unselect_all_button.pack()
        self.submit_button = tk.Button(left_frame, text="Save Configuration", command=self.submit_config)
        self.submit_button.pack(pady=(20, 0))

        # Right frame for new section
        right_frame = tk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        sample_label = tk.Label(right_frame, text="This is a sample label in the right frame")
        sample_label.pack()

        self.submit_button = tk.Button(
            self, text="Save Configuration", command=self.submit_config)
        self.submit_button.pack(pady=(20, 0)) 

    def submit_config(self):
        experiment_name = self.experiment_name_entry.get()  # Get the experiment name
        vpt = self.vpt_entry.get()
        rpv = self.rpv_entry.get()
        epm = self.epm_entry.get()
        llm_temp = self.llm_temp_entry.get()
        llm_epm = self.llm_epm_entry.get()

        msg = f"Experiment Name: {experiment_name}\nVariations per Template: {vpt}\nReformulations per Variation: {rpv}\nExperiments per Model (QG): {epm}\nExperiments per Model (LLM): {llm_epm}"
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
