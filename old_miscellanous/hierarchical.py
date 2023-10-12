import json

# Given JSON data
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

categories = ["llms", "optimization models", "tasks", "distribution", "ICL"]


def display_options(options):
    for key, value in options.items():
        print(f"{key}. {value}")
    print("e. Exit")


def hierarchical_selection(category_index, selections):
    while True:
        category = categories[category_index]
        print(f"\nSelect an option from {category}:")
        display_options(data[category])
        choice = input("Enter the number of your choice or e to exit: ")
        if choice == 'e':
            return
        selected = data[category].get(choice)
        if selected:
            selections[category] = selected
            if category_index < len(categories) - 1:
                hierarchical_selection(category_index + 1, selections)
                return


def save_selection(selections):
    with open('selections.json', 'w') as f:
        json.dump(selections, f, indent=4)


def main():
    selections = {}
    hierarchical_selection(0, selections)
    save_selection(selections)
    print("\nSelections saved to selections.json")


if __name__ == '__main__':
    main()
