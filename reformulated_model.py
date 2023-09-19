from gurobipy import Model, GRB

def knapsack_gurobi(W):
    # Create a new Gurobi model
    m = Model("knapsack_transform")

    # Decision variables
    x1 = m.addVar(vtype=GRB.BINARY, name="x1")
    x2 = m.addVar(vtype=GRB.BINARY, name="x2")
    x3 = m.addVar(vtype=GRB.BINARY, name="x3")
    x4 = m.addVar(vtype=GRB.BINARY, name="x4")

    # Objective function
    m.setObjective(20 * x1 + 30 * x2 + 50 * x3 + 10 * x4, GRB.MAXIMIZE)

    # Weight constraint
    m.addConstr(5 * x1 + 8 * x2 + 3 * x3 + 2 * x4 <= W, "weight_constraint")

    # Solve the model
    m.optimize()

    # Extract the solution
    selected_items = []
    if x1.X > 0.5: selected_items.append(0)
    if x2.X > 0.5: selected_items.append(1)
    if x3.X > 0.5: selected_items.append(2)
    if x4.X > 0.5: selected_items.append(3)


    return selected_items

# Data
W = 10
selected_items = knapsack_gurobi(W)
print(selected_items)
