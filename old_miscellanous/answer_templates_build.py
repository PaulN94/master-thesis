#1

from gurobipy import Model, GRB


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
values = {values}
weights = {weights}
W = {capacity}
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)

#2

from gurobipy import Model, GRB


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

    m.addConstr(x[{item_1}] + x[{item_2}] == 1, "item_1_or_item_2")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = {values}
weights = {weights}
W = {capacity}
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)

#3

from gurobipy import Model, GRB


def knapsack_gurobi(values, weights, W):
    n = len(values)
    m = Model("knapsack_transform")
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

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = {values}
weights = {weights}
W = {capacity}
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)

#4

from gurobipy import Model, GRB


def knapsack_gurobi(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack_transform")

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

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = {values}
weights = {weights}
W = {capacity}
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)

#5

from gurobipy import Model, GRB


def knapsack_gurobi(values, weights, W):
    # Number of items
    n = len(values)

    # Create a new Gurobi model
    m = Model("knapsack_transform")

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

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = {values}
weights = {weights}
W = {capacity}
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)

#6

from gurobipy import Model, GRB


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

    # Lower bound constraint
    m.addConstr(sum(x[i] for i in range(n)) >= {min_items}, "min_items_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = {values}
weights = {weights}
W = {capacity}
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)

#7

from gurobipy import Model, GRB


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

    # Force include item_1 in the backpack
    x[{item_1}].LB = 1  # Setting lower bound as 1

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = {values}
weights = {weights}
W = {capacity}
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)

#8

from gurobipy import Model, GRB


def knapsack_gurobi(values, weights, W, volumes, volume_limit):
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

    # Volume constraint
    m.addConstr(sum(volumes[i] * x[i] for i in range(n)) <= volume_limit, "volume_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = {values}
weights = {weights}
volumes = {volumes}  
volume_limit = {volume_limit}
W = {capacity}
selected_items = knapsack_gurobi(values, weights, W, volumes, volume_limit)
print(selected_items)

#9

from gurobipy import Model, GRB


def knapsack_gurobi(values, weights, W, time_costs, time_limit):
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

    # Time constraint
    m.addConstr(sum(time_costs[i] * x[i] for i in range(n)) <= time_limit, "time_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = {values}
weights = {weights}
time_costs = {time_costs}
time_limit = {time_limit}
W = {capacity}
selected_items = knapsack_gurobi(values, weights, W, time_costs, time_limit)
print(selected_items)

#10

from gurobipy import Model, GRB


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

    # Conflict constraints
    m.addConstr(x[{item_1}] + x[{item_3}] <= 1, f"conflict_{item_1}_{item_3}")
    m.addConstr(x[{item_2}] + x[{item_4}] <= 1, f"conflict_{item_2}_{item_4}")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = {values}
weights = {weights}
W = {capacity}
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)

