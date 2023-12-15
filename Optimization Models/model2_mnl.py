from gurobipy import Model, GRB, quicksum
import numpy as np

def mnl(utilities, revenues, k):
    # Number of products
    N = len(utilities)

    # Create a new Gurobi model
    m = Model("mnl")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables
    x = m.addVars(N, vtype=GRB.BINARY, name="x")
    t = m.addVar(vtype=GRB.CONTINUOUS, name="t")

    # Objective function
    m.setObjective(quicksum(revenues[i] * np.exp(utilities[i]) * x[i] * t for i in range(N)), GRB.MAXIMIZE)

    # Assortment size constraint
    m.addConstr(quicksum(x[i] for i in range(N)) <= k, "AssortmentSize")

    # Definition of t as the inverse of the sum in the denominator (Charnes-Cooper transformation)
    m.addConstr(t * (1 + quicksum(np.exp(utilities[j]) * x[j] for j in range(N))) == 1, "t_definition")

    # NonConvex parameter setting
    m.setParam('NonConvex', 2)

    # Solve the model
    m.optimize()

    # Check if a feasible solution was found
    if m.status == GRB.OPTIMAL:
        # Extract the solution
        selected_items = [i for i in range(N) if x[i].X > 0.5]
        objective_value = round(m.ObjVal)
    else:
        print("No optimal solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value

# Example data
N = 5  # Number of products
utilities = [0.8, 1.2, 0.5, 1.0, 1.4]  # Utility for each product
revenues = [12, 18, 11, 15, 22] # Revenue for each product
k = 3  # Maximum number of items in the assortment

selected_items, objective_value = mnl(utilities, revenues, k)

print("Selected items:", selected_items)
print("Objective value:", objective_value)