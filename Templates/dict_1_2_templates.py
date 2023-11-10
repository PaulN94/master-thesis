dict_1_2 = {
    "templates": [
        {
            "id": "1.2.1",
            "question_template": "Reformulate the optimization model to have a maximum allowed weight of {W}.",
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

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = m.ObjVal
        model_fingerprint = hex(m.Fingerprint & 0xFFFFFFFF)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None
        model_fingerprint = None

    return selected_items, objective_value, model_fingerprint


# Data
values = [33, 22, 30, 10, 40, 15, 25, 50, 45, 35]
weights = [5, 6, 8, 2, 7, 3, 4, 9, 8, 6]
W = {W}
selected_items, objective_value, fingerprint = knapsack_gurobi(values, weights, W)
print(selected_items)
            """,
            "answer_template_section": "W = {W}",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 30]
                }
            ]
        },
        {
            "id": "1.2.2",
            "question_template": "Reformulate the optimization model to account for the weight of the item with index {n} being set to {weight}.",
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

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = m.ObjVal
        model_fingerprint = hex(m.Fingerprint & 0xFFFFFFFF)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None
        model_fingerprint = None

    return selected_items, objective_value, model_fingerprint


# Data
values = [33, 22, 30, 10, 40, 15, 25, 50, 45, 35]
weights = [5, 6, 8, 2, 7, 3, 4, 9, 8, 6]
weights[{n}] = {weight}
W = 20
selected_items, objective_value, fingerprint = knapsack_gurobi(values, weights, W)
print(selected_items)
            """,
            "answer_template_section": "weights[{n}] = {weight}",
            "variables": [
                {
                    "name": "n",
                    "type": "int",
                    "range": [0, 9]
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
            "question_template": "Reformulate the optimization model so the item with index {n} has a value of {value}.",
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

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = m.ObjVal
        model_fingerprint = hex(m.Fingerprint & 0xFFFFFFFF)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None
        model_fingerprint = None

    return selected_items, objective_value, model_fingerprint


# Data
values = [33, 22, 30, 10, 40, 15, 25, 50, 45, 35]
values[{n}] = {value}
weights = [5, 6, 8, 2, 7, 3, 4, 9, 8, 6]
W = 20
selected_items, objective_value, fingerprint = knapsack_gurobi(values, weights, W)
print(selected_items)
            """,
            "answer_template_section": "values[{n}] = {value}",
            "variables": [
                {
                    "name": "n",
                    "type": "int",
                    "range": [0, 9]
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
            "question_template": "Reformulate the optimization model to include an L1 regularization with a penalty term of {lambda_value} for each selected item.",
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

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = m.ObjVal
        model_fingerprint = hex(m.Fingerprint & 0xFFFFFFFF)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None
        model_fingerprint = None

    return selected_items, objective_value, model_fingerprint


# Data
values = [33, 22, 30, 10, 40, 15, 25, 50, 45, 35]
weights = [5, 6, 8, 2, 7, 3, 4, 9, 8, 6]
W = 20
selected_items, objective_value, fingerprint = knapsack_gurobi(values, weights, W)
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
            "question_template": "Reformulate the optimization model to incorporate a synergy between items with indices {item_1} and {item_2}. When both are selected, a value of {add_value} is added.",
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

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = m.ObjVal
        model_fingerprint = hex(m.Fingerprint & 0xFFFFFFFF)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None
        model_fingerprint = None

    return selected_items, objective_value, model_fingerprint


# Data
values = [33, 22, 30, 10, 40, 15, 25, 50, 45, 35]
weights = [5, 6, 8, 2, 7, 3, 4, 9, 8, 6]
W = 20
selected_items, objective_value, fingerprint = knapsack_gurobi(values, weights, W)
print(selected_items)
            """,
            "answer_template_section": "m.setObjective(sum(values[i] * x[i] for i in range(n)) + {add_value} * x[{item_1}] * x[{item_2}], GRB.MAXIMIZE)",
            "variables": [
                {
                    "name": "item_1",
                    "type": "int",
                    "range": [0, 9],
                    "uniqueID": "1"
                },
                {
                    "name": "item_2",
                    "type": "int",
                    "range": [0, 9],
                    "uniqueID": "1"
                },
                {
                    "name": "add_value",
                    "type": "float",
                    "range": [10.0, 20.0]
                }
            ]
        },
        {
            "id": "1.2.6",
            "question_template": "Reformulate the optimization model to apply a penalty of {penalty} value units for each item selected after the one with index 1 in the array of selected items.",
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

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = m.ObjVal
        model_fingerprint = hex(m.Fingerprint & 0xFFFFFFFF)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None
        model_fingerprint = None

    return selected_items, objective_value, model_fingerprint


# Data
values = [33, 22, 30, 10, 40, 15, 25, 50, 45, 35]
weights = [5, 6, 8, 2, 7, 3, 4, 9, 8, 6]
W = 20
selected_items, objective_value, fingerprint = knapsack_gurobi(values, weights, W)
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
            "question_template": "Reformulate the optimization model to ensure that at least {min_items} items are selected.",
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

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = m.ObjVal
        model_fingerprint = hex(m.Fingerprint & 0xFFFFFFFF)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None
        model_fingerprint = None

    return selected_items, objective_value, model_fingerprint


# Data
values = [33, 22, 30, 10, 40, 15, 25, 50, 45, 35]
weights = [5, 6, 8, 2, 7, 3, 4, 9, 8, 6]
W = 20
selected_items, objective_value, fingerprint = knapsack_gurobi(values, weights, W)
print(selected_items)
            """,
            "answer_template_section": "m.addConstr(sum(x[i] for i in range(n)) >= {min_items})",
            "variables": [
                {
                    "name": "min_items",
                    "type": "int",
                    "range": [0, 5]
                }
            ]
        },
        {
            "id": "1.2.8",
            "question_template": "Reformulate the optimization model to make sure the item with the index {item_1} is mandatory in the knapsack.",
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

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = m.ObjVal
        model_fingerprint = hex(m.Fingerprint & 0xFFFFFFFF)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None
        model_fingerprint = None

    return selected_items, objective_value, model_fingerprint


# Data
values = [33, 22, 30, 10, 40, 15, 25, 50, 45, 35]
weights = [5, 6, 8, 2, 7, 3, 4, 9, 8, 6]
W = 20
selected_items, objective_value, fingerprint = knapsack_gurobi(values, weights, W)
print(selected_items)
            """,
            "answer_template_section": "m.addConstr(x[{item_1}] == 1",
            "variables": [
                {
                    "name": "item_1",
                    "type": "int",
                    "range": [0, 9]
                }
            ]
        },
        {
            "id": "1.2.9",
            "question_template": "Reformulate the optimization model to restrict the knapsack's contents to a maximum of {max_items} items.",
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

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = m.ObjVal
        model_fingerprint = hex(m.Fingerprint & 0xFFFFFFFF)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None
        model_fingerprint = None

    return selected_items, objective_value, model_fingerprint


# Data
values = [33, 22, 30, 10, 40, 15, 25, 50, 45, 35]
weights = [5, 6, 8, 2, 7, 3, 4, 9, 8, 6]
W = 20
selected_items, objective_value, fingerprint = knapsack_gurobi(values, weights, W)
print(selected_items)
            """,
            "answer_template_section": "m.addConstr(sum(x[i] for i in range(n)) <= {max_items})",
            "variables": [
                {
                    "name": "max_items",
                    "type": "int",
                    "range": [1, 5]
                }
            ]
        },
        {
            "id": "1.2.10",
            "question_template": "Reformulate the optimization model to guarantee that either the item with the index {item_1} or the item with index {item_2} is included, but not both.",
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

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = m.ObjVal
        model_fingerprint = hex(m.Fingerprint & 0xFFFFFFFF)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None
        model_fingerprint = None

    return selected_items, objective_value, model_fingerprint


# Data
values = [33, 22, 30, 10, 40, 15, 25, 50, 45, 35]
weights = [5, 6, 8, 2, 7, 3, 4, 9, 8, 6]
W = 20
selected_items, objective_value, fingerprint = knapsack_gurobi(values, weights, W)
print(selected_items)
            """,
            "answer_template_section": "m.addConstr(x[{item_1}] + x[{item_2}] == 1)",
            "variables": [
                {
                    "name": "item_1",
                    "type": "int",
                    "range": [0, 9],
                    "uniqueID": "1"
                },
                {
                    "name": "item_2",
                    "type": "int",
                    "range": [0, 9],
                    "uniqueID": "1"
                },
            ]
        }
    ]
}
