from gurobipy import Model, GRB, quicksum
import numpy as np  # Ensure that numpy is imported

# Specified example data
N = 3  # Total number of products
utilities = [0.5, 1.0, 1.5]  # Utility for each product
revenues = [10, 15, 20]  # Revenue for each product
k = 2  # Maximum number of items in the assortment

# Create a new model
m = Model("assortment_optimization")

# Add variables
x = m.addVars(N, vtype=GRB.BINARY, name="x")
t = m.addVar(vtype=GRB.CONTINUOUS, name="t")

# Set the objective
m.setObjective(quicksum(revenues[i] * np.exp(utilities[i]) * t * x[i] for i in range(N)), GRB.MAXIMIZE)

# Add constraint for the new variable 't'
m.addConstr(t * (1 + quicksum(np.exp(utilities[i]) * x[i] for i in range(N))) == 1, "denominator")

# Add constraint for the maximum number of items in the assortment
m.addConstr(quicksum(x[i] for i in range(N)) <= k, "assortment_size")

# Set the NonConvex parameter to allow solving of non-convex problems
m.setParam('NonConvex', 2)

# Optimize model
m.optimize()

# Display results
if m.status == GRB.OPTIMAL:
    print(f'Optimal objective: {m.objVal:.4f}')
    for i in range(N):
        print(f'Product {i}: {x[i].X}')
    print(f't: {t.X}')
else:
    print("No optimal solution found")
