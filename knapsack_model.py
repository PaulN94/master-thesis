#Answer templates

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
    m.setObjective(sum(values[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

    # Weight constraint
    m.m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [20, 30, 50, 10]
weights = [5, 8, 3, 2]
W = {W}
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

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [20, 30, 50, 10]
weights[{n}] = {weight}
weights = [5, 8, 3, 2]
W = 10
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)

#3


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

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [20, 30, 50, 10]
values[n] = {value}
weights = [5, 8, 3, 2]
W = 10
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
values = [20, 30, 50, 10]
weights = [5, 8, 3, 2]
W = 10
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
    m.setObjective(sum(values[i] * x[i] for i in range(n)) + {add_value} * x[{item_x}] * x[{item_y}], GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [20, 30, 50, 10]
weights = [5, 8, 3, 2]
W = 10
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
    m.setObjective(sum(values[i] * x[i] for i in range(n)) - {penalty} * sum(x[i] for i in range(2, n)), GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(sum(weights[i] * x[i] for i in range(n)) <= W, "weight_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [20, 30, 50, 10]
weights = [5, 8, 3, 2]
W = 10
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

    # Minimum items constraint
    m.addConstr(sum(x[i] for i in range(n)) >= {min_items}, "min_items_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [20, 30, 50, 10]
weights = [5, 8, 3, 2]
W = 10
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)

#8


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

    # Mandatory item constraint
    m.addConstr(x[{n}] == 1, "mandatory_item_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [20, 30, 50, 10]
weights = [5, 8, 3, 2]
W = 10
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)

#9


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

    # Maximum items constraint
    m.addConstr(sum(x[i] for i in range(n)) <= {max_items}, "max_items_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [20, 30, 50, 10]
weights = [5, 8, 3, 2]
W = 10
selected_items = knapsack_gurobi(values, weights, W)
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

    # Either or constraint
    m.addConstr(x[{i}] + x[{j}] <= 1)

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = [i for i in range(n) if x[i].X > 0.5]

    return selected_items


# Data
values = [20, 30, 50, 10]
weights = [5, 8, 3, 2]
W = 10
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)