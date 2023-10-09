import tkinter as tk
from tkinter import ttk, messagebox, font  # Importing font
import json


class IntegratedApp(tk.Tk):
    def __init__(self, data):
        super().__init__()

        self.title_font = font.Font(family="Helvetica", size=14, underline=1)  # Creating a font object

        self.data = data
        self.title("Question generation")
        self.geometry("600x800")

        # Question Generation Section
        self.config_label = tk.Label(self, text="Configuration:", font=self.title_font)  # Applying the font object
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

        self.submit_button = tk.Button(
            self, text="Save Configuration", command=self.submit_config)
        self.submit_button.pack(pady=(20, 0)) 

    def submit_config(self):
        
        vpt = self.vpt_entry.get()
        rpv = self.rpv_entry.get()
        epm = self.epm_entry.get()

        msg = f"Variations per Template: {vpt}\nReformulations per Variation: {rpv}\nExperiments per Model (QG): {epm}\n"
        messagebox.showinfo("Input Values", msg)

        # 1. Collecting data from input fields
        config = {
            "variations_per_template": self.vpt_entry.get(),
            "reformulations_per_variation": self.rpv_entry.get(),
            "experiments_per_model": self.epm_entry.get()
        }

        # 2. Convert treeview data to hierarchical format
        llms_data = {}
        for llm in self.tree.get_children(''):
            llm_name = self.tree.item(llm, "text")
            llms_data[llm_name] = {
                "select": self.tree.set(llm, 'check') == '✔',
                "optimization_models": {}
            }
            for model in self.tree.get_children(llm):
                model_name = self.tree.item(model, "text")
                llms_data[llm_name]["optimization_models"][model_name] = {
                    "select": self.tree.set(model, 'check') == '✔',
                    "tasks": {}
                }
                for task in self.tree.get_children(model):
                    task_name = self.tree.item(task, "text")
                    llms_data[llm_name]["optimization_models"][model_name]["tasks"][task_name] = {
                        "select": self.tree.set(task, 'check') == '✔',
                        "distribution": {}
                    }
                    for dist in self.tree.get_children(task):
                        dist_name = self.tree.item(dist, "text")
                        llms_data[llm_name]["optimization_models"][model_name]["tasks"][task_name]["distribution"][dist_name] = {
                            "select": self.tree.set(dist, 'check') == '✔',
                            "ICL": {}
                        }
                        for icl in self.tree.get_children(dist):
                            icl_name = self.tree.item(icl, "text")
                            llms_data[llm_name]["optimization_models"][model_name]["tasks"][task_name]["distribution"][dist_name]["ICL"][icl_name] = {
                                "select": self.tree.set(icl, 'check') == '✔'
                            }

        # Add the llms_data to the config dictionary
        config["llms"] = llms_data

        # 3. Save data to a JSON file
        with open("question_generation_config.json", "w") as outfile:
            json.dump(config, outfile, indent=4)

        messagebox.showinfo("Info", "Configuration saved successfully!")

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
            # Update all children based on parent's state
            self.update_children(item, check)
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
        "10": "ICL10: Ten-shot"
    }
}

app = IntegratedApp(data)
app.mainloop()
