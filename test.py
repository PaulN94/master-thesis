import json
import random

# Load the JSON data from the file
with open('example.json', 'r') as file:
    templates_data = json.load(file)

def generate_random_question():
    template = random.choice(templates_data['templates'])
    variables = {}
    for var in template['variables']:
        if var['type'] == 'int':
            value = random.randint(var['range'][0], var['range'][1])
            variables[var['name']] = value
        elif var['type'] == 'float':
            value = random.uniform(var['range'][0], var['range'][1])
            variables[var['name']] = round(value, 2)
        elif var['type'] == 'choice':
            value = random.choice(var['options'])
            variables[var['name']] = value

    question = template['question_template'].format(**variables)
    return question

# Generate a random question
print(generate_random_question())
