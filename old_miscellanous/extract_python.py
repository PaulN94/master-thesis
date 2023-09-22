import json

# JSON-Datei einlesen
with open('dict1_q_and_a_variations_knapsack_transformation.json', 'r') as f:
    data = json.load(f)

# Durch alle Einträge im "variations"-Array gehen und jeweils eine .py-Datei erstellen
for entry in data['variations']:
    filename = f"{entry['id']}.py"  # Verwendung der ID als Dateiname
    with open(filename, 'w') as f:
        f.write(entry['answer_variation'])
