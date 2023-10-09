import random
import json

from dict_1_2_templates_knapsack_transform import dict_1_2

# Create an empty dictionary to store the generated questions and answers
generated_questions = dict(variations=[])

# Loop through each template
for template in dict_1_2['templates']:
    template_id = template['id']
    question_template = template['question_template']
    answer_template = template['answer_template']
    answer_template_section = template.get('answer_template_section', "")
    variables = template['variables']

    # Variable values storage for use in arrayLength and uniqueID
    variable_values = {}
    unique_id_values = {}

    # Generate 3 variations for each template
    for i in range(1, 4):
        new_id = f"{template_id}.{i}"
        new_question = question_template
        new_answer = answer_template
        new_answer_section = answer_template_section

        # Fill in the placeholders in the question and answer
        for variable in variables:
            var_name = variable['name']
            var_type = variable['type']
            unique_id = variable.get('uniqueID')

            if var_type == "int":
                var_range = variable['range']
                if isinstance(var_range[1], dict):
                    var_range[1] = variable_values[var_range[1]['var']] - var_range[1].get('subtract', 0)
                var_value = random.randint(var_range[0], var_range[1])

                # Ensure uniqueness within the same uniqueID
                if unique_id:
                    while unique_id in unique_id_values and var_value in unique_id_values[unique_id]:
                        var_value = random.randint(var_range[0], var_range[1])
                    if unique_id not in unique_id_values:
                        unique_id_values[unique_id] = []
                    unique_id_values[unique_id].append(var_value)

            elif var_type == "float":
                var_range = variable['range']
                var_value = random.uniform(var_range[0], var_range[1])
                var_value = round(var_value, 2)
            elif var_type == "array":
                array_length = variable['arrayLength']
                if 'var' in array_length:
                    array_length = variable_values[array_length['var']]
                var_range = variable['range']
                var_value = [random.randint(var_range['min'], var_range['max']) for _ in range(array_length)]

            variable_values[var_name] = var_value  # store the value for future reference

            new_question = new_question.replace(f"{{{var_name}}}", str(var_value))
            new_answer = new_answer.replace(f"{{{var_name}}}", str(var_value))
            new_answer_section = new_answer_section.replace(f"{{{var_name}}}", str(var_value))

        # Reset unique_id_values for next iteration
        unique_id_values = {}

        # Add the new question and answer to the generated_questions dictionary
        new_variation = {
            "id": new_id,
            "question_variation": new_question,
            "answer_variation": new_answer,
        }
        if new_answer_section:
            new_variation["answer_section"] = new_answer_section
        generated_questions['variations'].append(new_variation)

# Save the generated_questions dictionary to a file in JSON format
with open('JSON1_variations_knapsack_transform.json', 'w') as f:
    json.dump(generated_questions, f, indent=4)
