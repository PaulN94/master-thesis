dict_2_2 = {
    "templates": [
        {
            "id": "2.2.1",
            "question_template": "Reformulate the optimization model to have a maximum number of products in the assortment of {k}.",
            "answer_template": """from gurobipy import Model, GRB, quicksum
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

selected_items, objective_value = mnl(utilities, prices, k)""",
            "variables": [
                {
                    "name": "k",
                    "type": "int",
                    "range": [1, 5]
                }
            ]
        },
        {
            "id": "2.2.2",
            "question_template": "Reformulate the optimization model to account for the utility of the products with index {n} being set to {utility}.",
            "answer_template": """from gurobipy import Model, GRB, quicksum
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

selected_items, objective_value = mnl(utilities, prices, k)""",
            "variables": [
                {
                    "name": "n",
                    "type": "int",
                    "range": [0, 4]
                },
                {
                    "name": "utility",
                    "type": "float",
                    "range": [0.5, 1.5]
                }
            ]
        },
        {
            "id": "2.2.3",
            "question_template": "Reformulate the optimization model so the products with index {n} has a price of {price}.",
            "answer_template": """from gurobipy import Model, GRB, quicksum
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

selected_items, objective_value = mnl(utilities, prices, k)""",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 30]
                }
            ]
        },
        {
            "id": "2.2.4",
            "question_template": "Reformulate the optimization model to ensure that at least {min_products} products are selected.",
            "answer_template": """from gurobipy import Model, GRB, quicksum
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

selected_items, objective_value = mnl(utilities, prices, k)""",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 30]
                }
            ]
        },
        {
            "id": "2.2.5",
            "question_template": "Reformulate the optimization model to make sure the product with the index {product_1} is mandatory in the assortment.",
            "answer_template": """from gurobipy import Model, GRB, quicksum
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

selected_items, objective_value = mnl(utilities, prices, k)""",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 30]
                }
            ]
        },
        {
            "id": "2.2.6",
            "question_template": "Reformulate the optimization model to ensure that the minimum utility of a selected products is at least {min_utility}.",
            "answer_template": """from gurobipy import Model, GRB, quicksum
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
""",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 30]
                }
            ]
        },
        {
            "id": "2.2.7",
            "question_template": "Reformulate the optimization model to guarantee that either the product with the index {product_1} or the product with index {product_2} is included in the assortment, but not both.",
            "answer_template": """from gurobipy import Model, GRB, quicksum
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

selected_items, objective_value = mnl(utilities, prices, k)""",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 30]
                }
            ]
        },
        {
            "id": "2.2.8",
            "question_template": "Reformulate the optimization model to include a penalty term of {penalty} for each selected item.",
            "answer_template": """from gurobipy import Model, GRB, quicksum
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

selected_items, objective_value = mnl(utilities, prices, k)""",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 30]
                }
            ]
        },
        {
            "id": "2.2.9",
            "question_template": "Reformulate the optimization model to incorporate a synergy between products with indices {product_1} and {product_2}. When both are selected, a revenue of {add_revenue} is added.",
            "answer_template": """from gurobipy import Model, GRB, quicksum
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

selected_items, objective_value = mnl(utilities, prices, k)""",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 30]
                }
            ]
        },
        {
            "id": "2.2.10",
            "question_template": "Reformulate the optimization model to include that the company wants to promote the product with the index {product_1} by giving double expected revenue weight, how would you adjust the objective function to reflect this.",
            "answer_template": """from gurobipy import Model, GRB, quicksum
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

selected_items, objective_value = mnl(utilities, prices, k)""",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 30]
                }
            ]
        }
    ]
}
