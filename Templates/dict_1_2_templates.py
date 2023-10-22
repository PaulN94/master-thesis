dict_1_2 = {
    "templates": [
        {
            "id": "1.2.1",
            "question_template": "Reformulate the code to have a maximum allowed weight of {W}.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack_gurobi(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack_transform")

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(sum(values[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [33, 22, 30, 10]
weights = [5, 6, 8, 2]
W = {W}
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)
            """,
            "answer_template_section": "W = {W}",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 10]
                }
            ]
        },
        {
            "id": "1.2.2",
            "question_template": "Reformulate the code to account for the weight of the item with index {n} being set to {weight}.",
            "answer_template": """from gurobipy import Model, GRB

            
def knapsack_gurobi(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack_transform")

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(sum(values[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [33, 22, 30, 10]
weights = [5, 6, 8, 2]
weights[{n}] = {weight}
W = 10
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)
            """,
            "answer_template_section": "weights[{n}] = {weight}",
            "variables": [
                {
                    "name": "n",
                    "type": "int",
                    "range": [0, 3]
                },
                {
                    "name": "weight",
                    "type": "int",
                    "range": [1, 10]
                }
            ]
        },
        {
            "id": "1.2.3",
            "question_template": "Reformulate the code so the item with index {n} has a value of {value}.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack_gurobi(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack_transform")

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(sum(values[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [33, 22, 30, 10]
values[{n}] = {value}
weights = [5, 6, 8, 2]
W = 10
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)
            """,
            "answer_template_section": "values[{n}] = {value}",
            "variables": [
                {
                    "name": "n",
                    "type": "int",
                    "range": [0, 3]
                },
                {
                    "name": "value",
                    "type": "int",
                    "range": [10, 50]
                }
            ]
        },
        {
            "id": "1.2.4",
            "question_template": "Reformulate the code to include an L1 regularization with a penalty term of {lambda_value} for each selected item.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack_gurobi(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack_transform")

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(sum(values[i] * x[i] for i in range(n)) - {lambda_value} * sum(x[i] for i in range(n)), GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [33, 22, 30, 10]
weights = [5, 6, 8, 2]
W = 10
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)
            """,
            "answer_template_section": "m.setObjective(sum(values[i] * x[i] for i in range(n)) - {lambda_value} * sum(x[i] for i in range(n)), GRB.MAXIMIZE)",
            "variables": [
                {
                    "name": "lambda_value",
                    "type": "float",
                    "range": [1.0, 10.0]
                }
            ]
        },
        {
            "id": "1.2.5",
            "question_template": "Reformulate the code to incorporate a synergy between items with indices {item_1} and {item_2}. When both are selected, a value of {add_value} is added.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack_gurobi(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack_transform")

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(sum(values[i] * x[i] for i in range(n)) + {add_value} * x[{item_1}] * x[{item_2}], GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [33, 22, 30, 10]
weights = [5, 6, 8, 2]
W = 10
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)
            """,
            "answer_template_section": "m.setObjective(sum(values[i] * x[i] for i in range(n)) + {add_value} * x[{item_1}] * x[{item_2}], GRB.MAXIMIZE)",
            "variables": [
                {
                    "name": "item_1",
                    "type": "int",
                    "range": [0, 3],
                    "uniqueID": "1"
                },
                {
                    "name": "item_2",
                    "type": "int",
                    "range": [0, 3],
                    "uniqueID": "1"
                },
                {
                    "name": "add_value",
                    "type": "float",
                    "range": [0.1, 10.0]
                }
            ]
        },
        {
            "id": "1.2.6",
            "question_template": "Reformulate the code to apply a penalty of {penalty} units for each item selected after the one with index 1 in the array of selected items.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack_gurobi(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack_transform")

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(sum(values[i] * x[i] for i in range(n)) - {penalty} * sum(x[i] for i in range(2, n)), GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [33, 22, 30, 10]
weights = [5, 6, 8, 2]
W = 10
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)
            """,
            "answer_template_section": "m.setObjective(sum(values[i] * x[i] for i in range(n)) - {penalty} * sum(x[i] for i in range(2, n)), GRB.MAXIMIZE)",
            "variables": [
                {
                    "name": "penalty",
                    "type": "float",
                    "range": [5, 15]
                }
            ]
        },
        {
            "id": "1.2.7",
            "question_template": "Reformulate the code to ensure that at least {min_items} items are selected.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack_gurobi(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack_transform")

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(sum(values[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Minimum items constraint
    m.addConstr(sum(x[i] for i in range(n)) >= {min_items}, "min_items_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [33, 22, 30, 10]
weights = [5, 6, 8, 2]
W = 10
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)
            """,
            "answer_template_section": "m.addConstr(sum(x[i] for i in range(n)) >= {min_items})",
            "variables": [
                {
                    "name": "min_items",
                    "type": "int",
                    "range": [1, 1]
                }
            ]
        },
        {
            "id": "1.2.8",
            "question_template": "Reformulate the code to make sure the item with the index {item_1} is mandatory in the knapsack.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack_gurobi(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack_transform")

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(sum(values[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Mandatory item constraint
    m.addConstr(x[{item_1}] == 1, "mandatory_item_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [33, 22, 30, 10]
weights = [5, 6, 8, 2]
W = 10
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)
            """,
            "answer_template_section": "m.addConstr(x[{item_1}] == 1",
            "variables": [
                {
                    "name": "item_1",
                    "type": "int",
                    "range": [0, 3]
                }
            ]
        },
        {
            "id": "1.2.9",
            "question_template": "Reformulate the code to restrict the knapsack's contents to a maximum of {max_items} items.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack_gurobi(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack_transform")

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(sum(values[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Maximum items constraint
    m.addConstr(sum(x[i] for i in range(n)) <= {max_items}, "max_items_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [33, 22, 30, 10]
weights = [5, 6, 8, 2]
W = 10
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)
            """,
            "answer_template_section": "m.addConstr(sum(x[i] for i in range(n)) <= {max_items})",
            "variables": [
                {
                    "name": "max_items",
                    "type": "int",
                    "range": [1, 3]
                }
            ]
        },
        {
            "id": "1.2.10",
            "question_template": "Reformulate the code to guarantee that either the item with the index {item_1} or the item with index {item_2} is included, but not both.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack_gurobi(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack_transform")

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(sum(values[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Either or constraint
    m.addConstr(x[{item_1}] + x[{item_2}] == 1)

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [33, 22, 30, 10]
weights = [5, 6, 8, 2]
W = 10
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)
            """,
            "answer_template_section": "m.addConstr(x[{item_1}] + x[{item_2}] == 1)",
            "variables": [
                {
                    "name": "item_1",
                    "type": "int",
                    "range": [0, 3],
                    "uniqueID": "1"
                },
                {
                    "name": "item_2",
                    "type": "int",
                    "range": [0, 3],
                    "uniqueID": "1"
                },
            ]
        }
    ]
}
