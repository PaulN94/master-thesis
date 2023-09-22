dict0 = {
    "templates": [
        {
            "id": "1.2.1",
            "question_template": "What would happen if the maximum allowed weight is changed to {W}?",
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
                    "range": [1, 10]
                }
            ]
        },
        {
            "id": "1.2.2",
            "question_template": "What would be the effect on the selection if the weight of the item with the index {n} was changed to {weight}?",
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
            "question_template": "If the value of the item with the index {n} is updated to {value}, how would the optimal selection be influenced?",
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
            "question_template": "How would you modify the objective function of the given knapsack problem to incorporate an L1 regularization, aiming to reduce the number of selected items, by adding a penalty term of {lambda_value} for each selected item?",
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
            "question_template": "Imagine there's a synergy between the items with the idices {item_x} and {item_y} such that if both are selected, an additional value of {add_value} is added to the objective. How can you model this effect in the objective function?",
            "answer_template": """from gurobipy import Model, GRB


def knapsack_gurobi(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack_transform")

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(sum(values[i] * x[i] for i in range(n)) + {add_value} * x[{item_x}] * x[{item_y}], GRB.MAXIMIZE)

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
            "answer_template_section": "m.setObjective(sum(values[i] * x[i] for i in range(n)) + {add_value} * x[{item_x}] * x[{item_y}], GRB.MAXIMIZE)",
            "variables": [
                {
                    "name": "item_x",
                    "type": "int",
                    "range": [0, 3]
                },
                {
                    "name": "item_y",
                    "type": "int",
                    "range": [0, 3]
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
            "question_template": "Imagine a scenario where a penalty of {penalty} units is applied for each additional item after the item with the index 1. How would you modify the objective function to account for this?",
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
            "question_template": "How does the model change if we introduce a lower bound constraint such that at least {min_items} items must be selected?",
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
                    "range": [1, 3]
                }
            ]
        },
        {
            "id": "1.2.8",
            "question_template": "Given that the item with the index {n} is mandatory in the knapsack, how would the remaining items be optimally selected?",
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
    m.addConstr(x[{n}] == 1, "mandatory_item_constraint")

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
            "answer_template_section": "m.addConstr(x[{n}] == 1",
            "variables": [
                {
                    "name": "n",
                    "type": "int",
                    "range": [0, 3]
                }
            ]
        },
        {
            "id": "1.2.9",
            "question_template": "If you were to restrict the number of items in the knapsack to a maximum of {max_items}, how would that influence the solution?",
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
            "question_template": "If there's a requirement that either item with index {i} or item with index {j} must be included in the knapsack but not both, how would you adjust the model to ensure this condition is met?",
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
    m.addConstr(x[{i}] + x[{j}] <= 1)

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
            "answer_template_section": "m.addConstr(x[{i}] + x[{j}] <= 1)",
            "variables": [
                {
                    "name": "i_j_pair",
                    "type": "object",
                    "values": [
                        {"i": 0, "j": 1},
                        {"i": 0, "j": 2},
                        {"i": 0, "j": 3},
                        {"i": 1, "j": 0},
                        {"i": 1, "j": 2},
                        {"i": 1, "j": 3},
                        {"i": 2, "j": 0},
                        {"i": 2, "j": 1},
                        {"i": 2, "j": 3},
                        {"i": 3, "j": 0},
                        {"i": 3, "j": 1},
                        {"i": 3, "j": 2}
                    ]
                }
            ]
        }
    ]
}
