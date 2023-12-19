#1

from gurobipy import Model, GRB, quicksum
import numpy as np

def mnl(utilities, prices, k):
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
    m.setObjective(quicksum(prices[i] * np.exp(utilities[i]) * x[i] * t for i in range(N)), GRB.MAXIMIZE)

    # Assortment size constraint
    m.addConstr(quicksum(x[i] for i in range(N)) <= k, "AssortmentSize")

    # Definition of t as the inverse of the sum in the denominator (to make it solvable by Gurobi)
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

# Data
utilities = [0.8, 1.2, 0.5, 1.0, 1.4]  # Utility for each product
prices = [12, 18, 11, 15, 22] # Prices of each product
k = {k}  # Maximum number of items in the assortment

selected_items, objective_value = mnl(utilities, prices, k)








#2

from gurobipy import Model, GRB, quicksum
import numpy as np

def mnl(utilities, prices, k):
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
    m.setObjective(quicksum(prices[i] * np.exp(utilities[i]) * x[i] * t for i in range(N)), GRB.MAXIMIZE)

    # Assortment size constraint
    m.addConstr(quicksum(x[i] for i in range(N)) <= k, "AssortmentSize")

    # Definition of t as the inverse of the sum in the denominator (to make it solvable by Gurobi)
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

# Data
utilities = [0.8, 1.2, 0.5, 1.0, 1.4]  # Utility for each product
utilities[{n}] = {utility} 
prices = [12, 18, 11, 15, 22] # Prices of each product
k = 3  # Maximum number of items in the assortment

selected_items, objective_value = mnl(utilities, prices, k)












#3

from gurobipy import Model, GRB, quicksum
import numpy as np

def mnl(utilities, prices, k):
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
    m.setObjective(quicksum(prices[i] * np.exp(utilities[i]) * x[i] * t for i in range(N)), GRB.MAXIMIZE)

    # Assortment size constraint
    m.addConstr(quicksum(x[i] for i in range(N)) <= k, "AssortmentSize")

    # Definition of t as the inverse of the sum in the denominator (to make it solvable by Gurobi)
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

# Data
utilities = [0.8, 1.2, 0.5, 1.0, 1.4]  # Utility for each product
prices = [12, 18, 11, 15, 22] # Prices of each product
prices[{n}] = {prices}
k = 3  # Maximum number of items in the assortment

selected_items, objective_value = mnl(utilities, prices, k)










#4

from gurobipy import Model, GRB, quicksum
import numpy as np

def mnl(utilities, prices, k):
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
    m.setObjective(quicksum(prices[i] * np.exp(utilities[i]) * x[i] * t for i in range(N)), GRB.MAXIMIZE)

    # Assortment size constraint
    m.addConstr(quicksum(x[i] for i in range(N)) <= k, "AssortmentSize")

    # Min assortment size constraint
    m.addConstr(quicksum(x[i] for i in range(N)) >= {min_products}, "MinAssortmentSize")

    # Definition of t as the inverse of the sum in the denominator (to make it solvable by Gurobi)
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

# Data
utilities = [0.8, 1.2, 0.5, 1.0, 1.4]  # Utility for each product
prices = [12, 18, 11, 15, 22] # Prices of each product
k = 3  # Maximum number of items in the assortment

selected_items, objective_value = mnl(utilities, prices, k)












#5

from gurobipy import Model, GRB, quicksum
import numpy as np

def mnl(utilities, prices, k):
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
    m.setObjective(quicksum(prices[i] * np.exp(utilities[i]) * x[i] * t for i in range(N)), GRB.MAXIMIZE)

    # Assortment size constraint
    m.addConstr(quicksum(x[i] for i in range(N)) <= k, "AssortmentSize")

    # Mandatory product constraint
    m.addConstr(x[{product_1}] == 1, "MandatoryProduct")

    # Definition of t as the inverse of the sum in the denominator (to make it solvable by Gurobi)
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

# Data
utilities = [0.8, 1.2, 0.5, 1.0, 1.4]  # Utility for each product
prices = [12, 18, 11, 15, 22] # Prices of each product
k = 3  # Maximum number of items in the assortment

selected_items, objective_value = mnl(utilities, prices, k)













#6

from gurobipy import Model, GRB, quicksum
import numpy as np

def mnl(utilities, prices, k):
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
    m.setObjective(quicksum(prices[i] * np.exp(utilities[i]) * x[i] * t for i in range(N)), GRB.MAXIMIZE)

    # Assortment size constraint
    m.addConstr(quicksum(x[i] for i in range(N)) <= k, "AssortmentSize")

    # Definition of t as the inverse of the sum in the denominator (to make it solvable by Gurobi)
    m.addConstr(t * (1 + quicksum(np.exp(utilities[j]) * x[j] for j in range(N))) == 1, "t_definition")

    # Min utility product constraint
    for i in range(N):
        m.addConstr(utilities[i] * x[i] >= {min_utility} * x[i], "MinimumUtilityConstraint")

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

# Data
utilities = [0.8, 1.2, 0.5, 1.0, 1.4]  # Utility for each product
prices = [12, 18, 11, 15, 22] # Prices of each product
k = 3  # Maximum number of items in the assortment

selected_items, objective_value = mnl(utilities, prices, k)












#7

from gurobipy import Model, GRB, quicksum
import numpy as np

def mnl(utilities, prices, k):
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
    m.setObjective(quicksum(prices[i] * np.exp(utilities[i]) * x[i] * t for i in range(N)), GRB.MAXIMIZE)

    # Assortment size constraint
    m.addConstr(quicksum(x[i] for i in range(N)) <= k, "AssortmentSize")

    # Definition of t as the inverse of the sum in the denominator (to make it solvable by Gurobi)
    m.addConstr(t * (1 + quicksum(np.exp(utilities[j]) * x[j] for j in range(N))) == 1, "t_definition")

    # Exclusive choice constraint
    m.addConstr(x[{product_1}] + x[{product_2}] == 1, "ExclusiveChoice")

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

# Data
utilities = [0.8, 1.2, 0.5, 1.0, 1.4]  # Utility for each product
prices = [12, 18, 11, 15, 22] # Prices of each product
k = 3  # Maximum number of items in the assortment

selected_items, objective_value = mnl(utilities, prices, k)













#8

from gurobipy import Model, GRB, quicksum
import numpy as np

def mnl(utilities, prices, k):
    # Number of products
    N = len(utilities)

    # Create a new Gurobi model
    m = Model("mnl")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables
    x = m.addVars(N, vtype=GRB.BINARY, name="x")
    t = m.addVar(vtype=GRB.CONTINUOUS, name="t")

    # Objective function with penalization term
    m.setObjective(quicksum(prices[i] * np.exp(utilities[i]) * x[i] * t for i in range(N)) - {penalty} * quicksum(x[i] for i in range(N)), GRB.MAXIMIZE)

    # Assortment size constraint
    m.addConstr(quicksum(x[i] for i in range(N)) <= k, "AssortmentSize")

    # Definition of t as the inverse of the sum in the denominator (to make it solvable by Gurobi)
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

# Data
utilities = [0.8, 1.2, 0.5, 1.0, 1.4]  # Utility for each product
prices = [12, 18, 11, 15, 22] # Prices of each product
k = 3  # Maximum number of items in the assortment

selected_items, objective_value = mnl(utilities, prices, k)
















#9

from gurobipy import Model, GRB, quicksum
import numpy as np

def mnl(utilities, prices, k):
    # Number of products
    N = len(utilities)

    # Create a new Gurobi model
    m = Model("mnl")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables
    x = m.addVars(N, vtype=GRB.BINARY, name="x")
    t = m.addVar(vtype=GRB.CONTINUOUS, name="t")

    # Objective function with additional revenue term
    m.setObjective(quicksum(prices[i] * np.exp(utilities[i]) * x[i] * t for i in range(N)) + {add_revenue} * x[{product_1}] * x[{product_2}], GRB.MAXIMIZE)

    # Assortment size constraint
    m.addConstr(quicksum(x[i] for i in range(N)) <= k, "AssortmentSize")

    # Definition of t as the inverse of the sum in the denominator (to make it solvable by Gurobi)
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

# Data
utilities = [0.8, 1.2, 0.5, 1.0, 1.4]  # Utility for each product
prices = [12, 18, 11, 15, 22] # Prices of each product
k = 3  # Maximum number of items in the assortment

selected_items, objective_value = mnl(utilities, prices, k)










#10

from gurobipy import Model, GRB, quicksum
import numpy as np

def mnl(utilities, prices, k):
    # Number of products
    N = len(utilities)

    # Create a new Gurobi model
    m = Model("mnl")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables
    x = m.addVars(N, vtype=GRB.BINARY, name="x")
    t = m.addVar(vtype=GRB.CONTINUOUS, name="t")

    # Objective function with double revenue term
    m.setObjective(quicksum(prices[i] * np.exp(utilities[i]) * x[i] * t for i in range(N)) + (prices[{product_1}] * np.exp(utilities[{product_1}]) * x[{product_1}] * t), GRB.MAXIMIZE)

    # Assortment size constraint
    m.addConstr(quicksum(x[i] for i in range(N)) <= k, "AssortmentSize")

    # Definition of t as the inverse of the sum in the denominator (to make it solvable by Gurobi)
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

# Data
utilities = [0.8, 1.2, 0.5, 1.0, 1.4]  # Utility for each product
prices = [12, 18, 11, 15, 22] # Prices of each product
k = 3  # Maximum number of items in the assortment

selected_items, objective_value = mnl(utilities, prices, k)