import random
import json

from dict0_q_a_templates_knapsack_transformation import dict0

# Create an empty dictionary to store the generated questions and answers
generated_questions = dict(variations=[])

# Loop through each template
for template in dict0['templates']:
    template_id = template['id']
    question_template = template['question_template']
    answer_template = template['answer_template']
    answer_template_section = template.get('answer_template_section', "")
    variables = template['variables']

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
            var_values = variable.get('values', variable.get('range', None))

            if var_values is None:
                continue

            if var_type == "int":
                var_value = random.randint(var_values[0], var_values[1])
            elif var_type == "float":
                var_value = random.uniform(var_values[0], var_values[1])
            elif var_type == "choice":
                var_value = random.choice(var_values)
            elif var_type == "object":
                var_value = random.choice(var_values)
                for key, value in var_value.items():
                    new_question = new_question.replace("{{{}}}".format(key), str(value))
                    new_answer = new_answer.replace("{{{}}}".format(key), str(value))
                    new_answer_section = new_answer_section.replace("{{{}}}".format(key), str(value))
                continue  # Skip the normal replacement for 'object' as it has multiple keys

            new_question = new_question.replace("{{{}}}".format(var_name), str(var_value))
            new_answer = new_answer.replace("{{{}}}".format(var_name), str(var_value))
            new_answer_section = new_answer_section.replace("{{{}}}".format(var_name), str(var_value))

        # Add the new question and answer to the generated_questions dictionary
        generated_questions['variations'].append({
            "id": new_id,
            "question_variation": new_question,
            "answer_variation": new_answer,
            "answer_section": new_answer_section,
        })

# Save the generated_questions dictionary to a file in JSON format
with open('JSON1_q_and_a_variations_knapsack_transformation.json', 'w') as f:
    json.dump(generated_questions, f, indent=4)