dict_1_1 = {
    "templates": [
        {
            "id": "1.1.1",
            "question_template": "Suppose we have {n} items with given values and weights. The values of the items are {values}, while the weights are {weights}. We have a backpack with a maximum carrying capacity of {capacity} weight units. There is a synergy between the items with the indices {item_1} and {item_2} such that if both are selected, an additional value of {add_value} is added to the objective (The indices start at 0). The task is to select the items to be placed in the backpack so that the total value of the items contained in the backpack is maximized without exceeding the weight limit. It is not allowed to divide the items: either an item is selected completely or not at all.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

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
        objective_value = round(m.ObjVal)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
values = {values}
weights = {weights}
W = {capacity}
selected_items, objective_value = knapsack(values, weights, W)
print(selected_items)""",
            "variables": [
                {
                    "name": "n",
                    "type": "int",
                    "range": [5, 10]
                },
                {
                    "name": "values",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 10,
                        "max": 40
                    }
                },
                {
                    "name": "weights",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 2,
                        "max": 8
                    }
                },
                {
                    "name": "capacity",
                    "type": "int",
                    "range": [5, 15]
                },
                {
                    "name": "item_1",
                    "type": "int",
                    "range": [0, {"var": "n", "subtract": 1}],
                    "uniqueID": "1"
                },
                {
                    "name": "item_2",
                    "type": "int",
                    "range": [0, {"var": "n", "subtract": 1}],
                    "uniqueID": "1"
                },
                {
                    "name": "add_value",
                    "type": "int",
                    "range": [1, 100]
                }
            ]
        },
        {
            "id": "1.1.2",
            "question_template": "Suppose we have {n} items with given values and weights. The values of the items are {values}, while the weights are {weights}. There is a requirement, that either the item with the index {item_1} or {item_2} must be included, but not both (The indices start at 0). We have a backpack with a maximum carrying capacity of {capacity} weight units. The task is to select the items to be placed in the backpack so that the total value of the items contained in the backpack is maximized without exceeding the weight limit. It is not allowed to divide the items: either an item is selected completely or not at all.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(sum(values[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    m.addConstr(x[{item_1}] + x[{item_2}] == 1, "item_1_or_item_2")

    # Solve the model
    m.optimize()

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = round(m.ObjVal)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
values = {values}
weights = {weights}
W = {capacity}
selected_items, objective_value = knapsack(values, weights, W)
print(selected_items)""",
            "variables": [
                {
                    "name": "n",
                    "type": "int",
                    "range": [5, 10]
                },
                {
                    "name": "values",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 10,
                        "max": 40
                    }
                },
                {
                    "name": "weights",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 2,
                        "max": 8
                    }
                },
                {
                    "name": "capacity",
                    "type": "int",
                    "range": [20, 25]
                },
                {
                    "name": "item_1",
                    "type": "int",
                    "range": [0, {"var": "n", "subtract": 1}],
                    "uniqueID": "1"
                },
                {
                    "name": "item_2",
                    "type": "int",
                    "range": [0, {"var": "n", "subtract": 1}],
                    "uniqueID": "1"
                }
            ]
        },

        {
            "id": "1.1.3",
            "question_template": "Suppose we have {n} items with given values and weights. The values of the items are {values}, while the weights are {weights}. We have a backpack with a maximum carrying capacity of {capacity} weight units. If the item with the index {item_1} is selected, the total weight of the items in the backpack is reduced by {weight_reduction}% (The indices start at 0). The task is to select the items to be placed in the backpack so that the total value of the items contained in the backpack is maximized without exceeding the weight limit. It is not allowed to divide the items: either an item is selected completely or not at all.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack(values, weights, W):
    n = len(values)
    m = Model("knapsack")
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Adjusting weights for item_1 selection
    adjusted_weights = [
        weights[i] if i != {item_1} else weights[i] * (1 - {weight_reduction} / 100) for i in range(n)
    ]

    m.setObjective(sum(values[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

    # add constraint for weight
    m.addConstr(sum(adjusted_weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # add indicator constraint
    m.addGenConstrIndicator(x[{item_1}], True, sum(weights[i] * x[i] for i in range(n)) <= W)

    m.optimize()

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = round(m.ObjVal)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
values = {values}
weights = {weights}
W = {capacity}
selected_items, objective_value = knapsack(values, weights, W)
print(selected_items)""",
            "variables": [
                {
                    "name": "n",
                    "type": "int",
                    "range": [5, 10]
                },
                {
                    "name": "values",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 10,
                        "max": 40
                    }
                },
                {
                    "name": "weights",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 2,
                        "max": 8
                    }
                },
                {
                    "name": "capacity",
                    "type": "int",
                    "range": [5, 15]
                },
                {
                    "name": "item_1",
                    "type": "int",
                    "range": [0, {"var": "n", "subtract": 1}]
                },
                {
                    "name": "weight_reduction",
                    "type": "int",
                    "range": [1, 100]
                }
            ]
        },

        {
            "id": "1.1.4",
            "question_template": "Suppose we have {n} items with given values and weights. The values of the items are {values} while the weights are {weights}. We have a backpack with a maximum carrying capacity of {capacity} weight units. If the amount of items in the backpack is only {amount} or less, its value is multiplied by {multiplier}.  The task is to select the items to be placed in the backpack so that the total value of the items contained in the backpack is maximized without exceeding the weight limit. It is not allowed to divide the items: either an item is selected completely or not at all.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")
    
    # Large constant
    M = 10000

    # Objective function with potential multiplier
    m.setObjective(
    sum(values[i] * x[i] for i in range(n)) * {multiplier} - M * (sum(x[i] for i in range(n)) - {amount}) ** 2,
    GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Solve the model
    m.optimize()

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = round(m.ObjVal)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
values = {values}
weights = {weights}
W = {capacity}
selected_items, objective_value = knapsack(values, weights, W)
print(selected_items)""",
            "variables": [
                {
                    "name": "n",
                    "type": "int",
                    "range": [5, 10]
                },
                {
                    "name": "values",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 10,
                        "max": 40
                    }
                },
                {
                    "name": "weights",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 2,
                        "max": 8
                    }
                },
                {
                    "name": "capacity",
                    "type": "int",
                    "range": [5, 15]
                },
                {
                    "name": "amount",
                    "type": "int",
                    "range": [1, {"var": "n", "subtract": 1}]
                },
                {
                    "name": "multiplier",
                    "type": "int",
                    "range": [1, 10]
                }
            ]
        },

        {
            "id": "1.1.5",
            "question_template": "Suppose we have {n} items with given values and weights. The values of the items are {values} while the weights are {weights}. We have a backpack with a maximum carrying capacity of {capacity} weight units. Selecting both the items with the indices {item_1} and {item_2} results in a reduction in total value of {value_reduction} (The indices start at 0). The task is to select the items to be placed in the backpack so that the total value of the items contained in the backpack is maximized without exceeding the weight limit. It is not allowed to divide the items: either an item is selected completely or not at all.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(
        sum(values[i] * x[i] for i in range(n)) - {value_reduction} * x[{item_1}] * x[{item_2}], 
        GRB.MAXIMIZE
    )

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Solve the model
    m.optimize()

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = round(m.ObjVal)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
values = {values}
weights = {weights}
W = {capacity}
selected_items, objective_value = knapsack(values, weights, W)
print(selected_items)""",
            "variables": [
                {
                    "name": "n",
                    "type": "int",
                    "range": [5, 10]
                },
                {
                    "name": "values",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 10,
                        "max": 40
                    }
                },
                {
                    "name": "weights",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 2,
                        "max": 8
                    }
                },
                {
                    "name": "capacity",
                    "type": "int",
                    "range": [5, 15]
                },
                {
                    "name": "item_1",
                    "type": "int",
                    "range": [0, {"var": "n", "subtract": 1}],
                    "uniqueID": "1"
                },
                {
                    "name": "item_2",
                    "type": "int",
                    "range": [0, {"var": "n", "subtract": 1}],
                    "uniqueID": "1"
                },
                {
                    "name": "value_reduction",
                    "type": "int",
                    "range": [1, 100]
                }
            ]
        },

        {
            "id": "1.1.6",
            "question_template": "Suppose we have {n} items with given values and weights. The values of the items are {values} while the weights are {weights}. We have a backpack with a maximum carrying capacity of {capacity} weight units. There is also a lower bound constraint, that {min_items} item(s) must be selected. The task is to select the items to be placed in the backpack so that the total value of the items contained in the backpack is maximized without exceeding the weight limit. It is not allowed to divide the items: either an item is selected completely or not at all.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(sum(values[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Lower bound constraint
    m.addConstr(sum(x[i] for i in range(n)) >= {min_items}, "min_items_constraint")

    # Solve the model
    m.optimize()

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = round(m.ObjVal)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
values = {values}
weights = {weights}
W = {capacity}
selected_items, objective_value = knapsack(values, weights, W)
print(selected_items)""",
            "variables": [
                {
                    "name": "n",
                    "type": "int",
                    "range": [5, 10]
                },
                {
                    "name": "values",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 10,
                        "max": 40
                    }
                },
                {
                    "name": "weights",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 2,
                        "max": 8
                    }
                },
                {
                    "name": "capacity",
                    "type": "int",
                    "range": [25, 30]
                },
                {
                    "name": "min_items",
                    "type": "int",
                    "range": [1, 3]
                }
            ]
        },

        {
            "id": "1.1.7",
            "question_template": "Suppose we have {n} items with given values and weights. The values of the items are {values} while the weights are {weights}. We have a backpack with a maximum carrying capacity of {capacity} weight units. The item with the index {item_1} must always be included in the backpack (The indices start at 0). The task is to select the items to be placed in the backpack so that the total value of the items contained in the backpack is maximized without exceeding the weight limit. It is not allowed to divide the items: either an item is selected completely or not at all.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(sum(values[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Force include item_1 in the backpack
    x[{item_1}].LB = 1  # Setting lower bound as 1

    # Solve the model
    m.optimize()

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = round(m.ObjVal)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
values = {values}
weights = {weights}
W = {capacity}
selected_items, objective_value = knapsack(values, weights, W)
print(selected_items)""",
            "variables": [
                {
                    "name": "n",
                    "type": "int",
                    "range": [5, 10]
                },
                {
                    "name": "values",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 10,
                        "max": 40
                    }
                },
                {
                    "name": "weights",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 2,
                        "max": 8
                    }
                },
                {
                    "name": "capacity",
                    "type": "int",
                    "range": [10, 15]
                },
                {
                    "name": "item_1",
                    "type": "int",
                    "range": [0, {"var": "n", "subtract": 1}]
                },
            ]
        },

        {
            "id": "1.1.8",
            "question_template": "Suppose we have {n} items with given values, weights, and volumes. The values of the items are {values} while the weights are {weights}, and the volumes are {volumes} volume units respectively. The backpack has a volume limit of {volume_limit} volume units along with a weight limit of {capacity} weight units. The task is to select the items to be placed in the backpack so that the total value of the items contained in the backpack is maximized without exceeding the weight or volume limit. It is not allowed to divide the items: either an item is selected completely or not at all.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack(values, weights, W, volumes, volume_limit):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(sum(values[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Volume constraint
    m.addConstr(sum(volumes[i] * x[i] for i in range(n)) <= volume_limit, "volume_constraint")

    # Solve the model
    m.optimize()

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = round(m.ObjVal)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
values = {values}
weights = {weights}
volumes = {volumes}  
volume_limit = {volume_limit}
W = {capacity}
selected_items, objective_value = knapsack(values, weights, W, volumes, volume_limit)
print(selected_items)""",
            "variables": [
                {
                    "name": "n",
                    "type": "int",
                    "range": [5, 10]
                },
                {
                    "name": "values",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 10,
                        "max": 40
                    }
                },
                {
                    "name": "weights",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 2,
                        "max": 8
                    }
                },
                {
                    "name": "capacity",
                    "type": "int",
                    "range": [5, 15]
                },
                {
                    "name": "volumes",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 5,
                        "max": 10
                    }
                },
                {
                    "name": "volume_limit",
                    "type": "int",
                    "range": [10, 15]
                }
            ]
        },

        {
            "id": "1.1.9",
            "question_template": "Suppose we have {n} items with given values, weights, and time costs. The values of the items are {values} while the weights are {weights}, and the time costs are {time_costs} time units respectively. The total time cannot exceed {time_limit} time units, and the weight limit is {capacity} weight units. The task is to select the items to be placed in the backpack so that the total value of the items contained in the backpack is maximized without exceeding the weight or time limit. It is not allowed to divide the items: either an item is selected completely or not at all.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack(values, weights, W, time_costs, time_limit):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(sum(values[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Time constraint
    m.addConstr(sum(time_costs[i] * x[i] for i in range(n)) <= time_limit, "time_constraint")

    # Solve the model
    m.optimize()

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = round(m.ObjVal)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
values = {values}
weights = {weights}
time_costs = {time_costs}
time_limit = {time_limit}
W = {capacity}
selected_items, objective_value = knapsack(values, weights, W, time_costs, time_limit)
print(selected_items)""",
            "variables": [
                {
                    "name": "n",
                    "type": "int",
                    "range": [5, 10]
                },
                {
                    "name": "values",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 10,
                        "max": 40
                    }
                },
                {
                    "name": "weights",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 2,
                        "max": 8
                    }
                },
                {
                    "name": "capacity",
                    "type": "int",
                    "range": [5, 15]
                },
                {
                    "name": "time_costs",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 1,
                        "max": 10
                    }
                },
                {
                    "name": "time_limit",
                    "type": "int",
                    "range": [10, 15]
                }
            ]
        },

        {
            "id": "1.1.10",
            "question_template": "Suppose we have {n} items with given values and weights. The values of the items are {values} while the weights are {weights}. We have a backpack with a maximum carrying capacity of {capacity} weight units. The combinations of the items with the indices {item_1} and {item_3} or {item_2} and {item_4} cannot be selected together in the backpack (The indices start at 0). The task is to select the items to be placed in the backpack so that the total value of the items contained in the backpack is maximized without exceeding the weight limit. It is not allowed to divide the items: either an item is selected completely or not at all.",
            "answer_template": """from gurobipy import Model, GRB


def knapsack(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(sum(values[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Conflict constraints
    m.addConstr(x[{item_1}] + x[{item_3}] <= 1, f"conflict_{item_1}_{item_3}")
    m.addConstr(x[{item_2}] + x[{item_4}] <= 1, f"conflict_{item_2}_{item_4}")

    # Solve the model
    m.optimize()

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(n) if x[i].X > 0.5]
        objective_value = round(m.ObjVal)
    else:
        print("No feasible solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
values = {values}
weights = {weights}
W = {capacity}
selected_items, objective_value = knapsack(values, weights, W)
print(selected_items)""",
            "variables": [
                {
                    "name": "n",
                    "type": "int",
                    "range": [5, 10]
                },
                {
                    "name": "values",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 10,
                        "max": 40
                    }
                },
                {
                    "name": "weights",
                    "type": "array",
                    "arrayLength": {"var": "n"},
                    "range": {
                        "min": 2,
                        "max": 8
                    }
                },
                {
                    "name": "capacity",
                    "type": "int",
                    "range": [5, 15]
                },
                {
                    "name": "item_1",
                    "type": "int",
                    "range": [0, {"var": "n", "subtract": 1}],
                    "uniqueID": "1"
                },
                {
                    "name": "item_2",
                    "type": "int",
                    "range": [0, {"var": "n", "subtract": 1}],
                    "uniqueID": "2"
                },
                {
                    "name": "item_3",
                    "type": "int",
                    "range": [0, {"var": "n", "subtract": 1}],
                    "uniqueID": "1"

                },
                {
                    "name": "item_4",
                    "type": "int",
                    "range": [0, {"var": "n", "subtract": 1}],
                    "uniqueID": "2"
                },
            ]
        }

    ]
}
