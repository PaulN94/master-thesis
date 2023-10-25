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
# The indices start at 0.
values = [33, 22, 30, 10, 40, 15, 25, 50, 45, 35]
weights = [5, 6, 8, 2, 7, 3, 4, 9, 8, 6]
W = 20
selected_items = knapsack_gurobi(values, weights, W)
print(selected_items)
