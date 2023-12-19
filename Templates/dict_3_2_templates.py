dict_3_2 = {
    "templates": [
        {
            "id": "3.2.1",
            "question_template": "Reformulate the optimization model so the product with index {n} has a visibility parameter of {visibility}.",
            "answer_template": """from gurobipy import Model, GRB, quicksum


def apv(prices, attraction_values, visibility_parameters, T):
    # Number of products
    n_products = len(prices)

    # Create a new Gurobi model
    m = Model("apv")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables: whether product i is in the assortment S_t for customer t
    x = m.addVars(T, n_products, vtype=GRB.BINARY, name="x")

    # New variable for the inverse of the denominator in the objective function
    y = m.addVars(T, name="y")

    # Objective function: Maximize total expected revenue
    # Non-linear term replaced by y[t]
    revenue = quicksum(prices[i] * attraction_values[i] * x[t, i] * y[t]
                       for t in range(T) for i in range(n_products))    
    m.setObjective(revenue, GRB.MAXIMIZE)

    # Constraints defining y[t] as the inverse of the sum in the denominator (to make it solvable by Gurobi)
    for t in range(T):
        m.addConstr(y[t] * (1 + quicksum(attraction_values[j] * x[t, j] for j in range(n_products))) == 1, "inverse_denominator")

    # Visibility constraints: each product i must be shown to at least visibility_parameters[i] customers
    for i in range(n_products):
        m.addConstr(quicksum(x[t, i] for t in range(T))
                    >= visibility_parameters[i], "visibility_constraint")

    # Solve the model
    m.setParam('NonConvex', 2)
    m.optimize()

    # Result handling
    if m.status == GRB.OPTIMAL:
        solution_x = m.getAttr('X', x)
        selected_items = [
            [i for i in range(n_products) if solution_x[t, i] > 0.5] for t in range(T)]
        objective_value = round(m.objVal)
    else:
        print("No optimal solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
prices = [20, 15, 40, 25, 50]  # Prices of products
attraction_values = [0.7, 0.8, 0.6, 0.9, 0.5]  # Attraction values for products
visibility_parameters = [2, 3, 1, 2, 2] # Minimum number of customers to show each product
visibility_parameters[{n}] = {visibility}
T = 10  # Number of customers

# Running the model
selected_items, objective_value = apv(prices, attraction_values, visibility_parameters, T)""",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 30]
                }
            ]
        },
        {
            "id": "3.2.2",
            "question_template": "Reformulate the optimization model to account for the price of the product with index {n} being set to {price}.",
            "answer_template": """from gurobipy import Model, GRB, quicksum


def apv(prices, attraction_values, visibility_parameters, T):
    # Number of products
    n_products = len(prices)

    # Create a new Gurobi model
    m = Model("apv")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables: whether product i is in the assortment S_t for customer t
    x = m.addVars(T, n_products, vtype=GRB.BINARY, name="x")

    # New variable for the inverse of the denominator in the objective function
    y = m.addVars(T, name="y")

    # Objective function: Maximize total expected revenue
    # Non-linear term replaced by y[t]
    revenue = quicksum(prices[i] * attraction_values[i] * x[t, i] * y[t]
                       for t in range(T) for i in range(n_products))    
    m.setObjective(revenue, GRB.MAXIMIZE)

    # Constraints defining y[t] as the inverse of the sum in the denominator (to make it solvable by Gurobi)
    for t in range(T):
        m.addConstr(y[t] * (1 + quicksum(attraction_values[j] * x[t, j] for j in range(n_products))) == 1, "inverse_denominator")

    # Visibility constraints: each product i must be shown to at least visibility_parameters[i] customers
    for i in range(n_products):
        m.addConstr(quicksum(x[t, i] for t in range(T))
                    >= visibility_parameters[i], "visibility_constraint")

    # Solve the model
    m.setParam('NonConvex', 2)
    m.optimize()

    # Result handling
    if m.status == GRB.OPTIMAL:
        solution_x = m.getAttr('X', x)
        selected_items = [
            [i for i in range(n_products) if solution_x[t, i] > 0.5] for t in range(T)]
        objective_value = round(m.objVal)
    else:
        print("No optimal solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
prices = [20, 15, 40, 25, 50]  # Prices of products
prices[{n}] = {price}
attraction_values = [0.7, 0.8, 0.6, 0.9, 0.5]  # Attraction values for products
visibility_parameters = [2, 3, 1, 2, 2] # Minimum number of customers to show each product
T = 10  # Number of customers

# Running the model
selected_items, objective_value = apv(prices, attraction_values, visibility_parameters, T)""",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 30]
                }
            ]
        },
        {
            "id": "3.2.3",
            "question_template": "Reformulate the optimization model so the product with index {n} has an attraction value of {attraction}.",
            "answer_template": """from gurobipy import Model, GRB, quicksum


def apv(prices, attraction_values, visibility_parameters, T):
    # Number of products
    n_products = len(prices)

    # Create a new Gurobi model
    m = Model("apv")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables: whether product i is in the assortment S_t for customer t
    x = m.addVars(T, n_products, vtype=GRB.BINARY, name="x")

    # New variable for the inverse of the denominator in the objective function
    y = m.addVars(T, name="y")

    # Objective function: Maximize total expected revenue
    # Non-linear term replaced by y[t]
    revenue = quicksum(prices[i] * attraction_values[i] * x[t, i] * y[t]
                       for t in range(T) for i in range(n_products))    
    m.setObjective(revenue, GRB.MAXIMIZE)

    # Constraints defining y[t] as the inverse of the sum in the denominator (to make it solvable by Gurobi)
    for t in range(T):
        m.addConstr(y[t] * (1 + quicksum(attraction_values[j] * x[t, j] for j in range(n_products))) == 1, "inverse_denominator")

    # Visibility constraints: each product i must be shown to at least visibility_parameters[i] customers
    for i in range(n_products):
        m.addConstr(quicksum(x[t, i] for t in range(T))
                    >= visibility_parameters[i], "visibility_constraint")

    # Solve the model
    m.setParam('NonConvex', 2)
    m.optimize()

    # Result handling
    if m.status == GRB.OPTIMAL:
        solution_x = m.getAttr('X', x)
        selected_items = [
            [i for i in range(n_products) if solution_x[t, i] > 0.5] for t in range(T)]
        objective_value = round(m.objVal)
    else:
        print("No optimal solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
prices = [20, 15, 40, 25, 50]  # Prices of products
attraction_values = [0.7, 0.8, 0.6, 0.9, 0.5]  # Attraction values for products
attraction_values[{n}] = {attraction}
visibility_parameters = [2, 3, 1, 2, 2] # Minimum number of customers to show each product
T = 10  # Number of customers

# Running the model
selected_items, objective_value = apv(prices, attraction_values, visibility_parameters, T)""",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 30]
                }
            ]
        },
        {
            "id": "3.2.4",
            "question_template": "Reformulate the optimization model to incorporate a constraint that ensures no more than {max_items} items are displayed to each customer.",
            "answer_template": """from gurobipy import Model, GRB, quicksum


def apv(prices, attraction_values, visibility_parameters, T):
    # Number of products
    n_products = len(prices)

    # Create a new Gurobi model
    m = Model("apv")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables: whether product i is in the assortment S_t for customer t
    x = m.addVars(T, n_products, vtype=GRB.BINARY, name="x")

    # New variable for the inverse of the denominator in the objective function
    y = m.addVars(T, name="y")

    # Maximum number of items per customer constraint
    for t in range(T):
        m.addConstr(quicksum(x[t, i] for i in range(n_products)) <= {max_items}, f"max_items_for_customer_{t}")

    # Objective function: Maximize total expected revenue
    # Non-linear term replaced by y[t]
    revenue = quicksum(prices[i] * attraction_values[i] * x[t, i] * y[t]
                       for t in range(T) for i in range(n_products))    
    m.setObjective(revenue, GRB.MAXIMIZE)

    # Constraints defining y[t] as the inverse of the sum in the denominator (to make it solvable by Gurobi)
    for t in range(T):
        m.addConstr(y[t] * (1 + quicksum(attraction_values[j] * x[t, j] for j in range(n_products))) == 1, "inverse_denominator")

    # Visibility constraints: each product i must be shown to at least visibility_parameters[i] customers
    for i in range(n_products):
        m.addConstr(quicksum(x[t, i] for t in range(T))
                    >= visibility_parameters[i], "visibility_constraint")

    # Solve the model
    m.setParam('NonConvex', 2)
    m.optimize()

    # Result handling
    if m.status == GRB.OPTIMAL:
        solution_x = m.getAttr('X', x)
        selected_items = [
            [i for i in range(n_products) if solution_x[t, i] > 0.5] for t in range(T)]
        objective_value = round(m.objVal)
    else:
        print("No optimal solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
prices = [20, 15, 40, 25, 50]  # Prices of products
attraction_values = [0.7, 0.8, 0.6, 0.9, 0.5]  # Attraction values for products
visibility_parameters = [2, 3, 1, 2, 2] # Minimum number of customers to show each product
T = 10  # Number of customers

# Running the model
selected_items, objective_value = apv(prices, attraction_values, visibility_parameters, T)""",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 30]
                }
            ]
        },
        {
            "id": "3.2.5",
            "question_template": "Reformulate the optimization model to introduce a budget constraint, where each displayed product causes a cost of {cost} the total cost of displayed products must not be exceeded {budget_limit}.",
            "answer_template": """from gurobipy import Model, GRB, quicksum


def apv(prices, attraction_values, visibility_parameters, T, cost, budget_limit):
    # Number of products
    n_products = len(prices)

    # Create a new Gurobi model
    m = Model("apv")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables: whether product i is in the assortment S_t for customer t
    x = m.addVars(T, n_products, vtype=GRB.BINARY, name="x")

    # New variable for the inverse of the denominator in the objective function
    y = m.addVars(T, name="y")

    # Objective function: Maximize total expected revenue
    # Non-linear term replaced by y[t]
    revenue = quicksum(prices[i] * attraction_values[i] * x[t, i] * y[t]
                       for t in range(T) for i in range(n_products))    
    m.setObjective(revenue, GRB.MAXIMIZE)

    # Constraints defining y[t] as the inverse of the sum in the denominator (to make it solvable by Gurobi)
    for t in range(T):
        m.addConstr(y[t] * (1 + quicksum(attraction_values[j] * x[t, j] for j in range(n_products))) == 1, "inverse_denominator")

    # Visibility constraints: each product i must be shown to at least visibility_parameters[i] customers
    for i in range(n_products):
        m.addConstr(quicksum(x[t, i] for t in range(T))
                    >= visibility_parameters[i], "visibility_constraint")
        
    # Budget constraint: The total cost of displayed items must not exceed the budget limit
    m.addConstr(quicksum(cost * x[t, i] for t in range(T) for i in range(n_products)) <= budget_limit, "budget_constraint")

    # Solve the model
    m.setParam('NonConvex', 2)
    m.optimize()

    # Result handling
    if m.status == GRB.OPTIMAL:
        solution_x = m.getAttr('X', x)
        selected_items = [
            [i for i in range(n_products) if solution_x[t, i] > 0.5] for t in range(T)]
        objective_value = round(m.objVal)
    else:
        print("No optimal solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
prices = [20, 15, 40, 25, 50]  # Prices of products
attraction_values = [0.7, 0.8, 0.6, 0.9, 0.5]  # Attraction values for products
visibility_parameters = [2, 3, 1, 2, 2] # Minimum number of customers to show each product
T = 10  # Number of customers

cost = {cost}  # Cost per displayed item
budget_limit = {budget_limit}  # Total budget limit

# Running the model
selected_items, objective_value = apv(prices, attraction_values, visibility_parameters, T, cost, budget_limit)""",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 30]
                }
            ]
        },
        {
            "id": "3.2.6",
            "question_template": "Reformulate the optimization model to ensure that at least {min_products} products are selected for each assortment.",
            "answer_template": """from gurobipy import Model, GRB, quicksum


def apv(prices, attraction_values, visibility_parameters, T):
    # Number of products
    n_products = len(prices)

    # Create a new Gurobi model
    m = Model("apv")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables: whether product i is in the assortment S_t for customer t
    x = m.addVars(T, n_products, vtype=GRB.BINARY, name="x")

    # New variable for the inverse of the denominator in the objective function
    y = m.addVars(T, name="y")

    # Objective function: Maximize total expected revenue
    # Non-linear term replaced by y[t]
    revenue = quicksum(prices[i] * attraction_values[i] * x[t, i] * y[t]
                       for t in range(T) for i in range(n_products))    
    m.setObjective(revenue, GRB.MAXIMIZE)

    # Constraints defining y[t] as the inverse of the sum in the denominator (to make it solvable by Gurobi)
    for t in range(T):
        m.addConstr(y[t] * (1 + quicksum(attraction_values[j] * x[t, j] for j in range(n_products))) == 1, "inverse_denominator")

    # Visibility constraints: each product i must be shown to at least visibility_parameters[i] customers
    for i in range(n_products):
        m.addConstr(quicksum(x[t, i] for t in range(T))
                    >= visibility_parameters[i], "visibility_constraint")
        
    # Minimum number of products per customer constraint
    for t in range(T):
        m.addConstr(quicksum(x[t, i] for i in range(n_products)) >= {min_products}, "Minimum_products_per_customer")


    # Solve the model
    m.setParam('NonConvex', 2)
    m.optimize()

    # Result handling
    if m.status == GRB.OPTIMAL:
        solution_x = m.getAttr('X', x)
        selected_items = [
            [i for i in range(n_products) if solution_x[t, i] > 0.5] for t in range(T)]
        objective_value = round(m.objVal)
    else:
        print("No optimal solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
prices = [20, 15, 40, 25, 50]  # Prices of products
attraction_values = [0.7, 0.8, 0.6, 0.9, 0.5]  # Attraction values for products
visibility_parameters = [2, 3, 1, 2, 2] # Minimum number of customers to show each product
T = 10  # Number of customers

# Running the model
selected_items, objective_value = apv(prices, attraction_values, visibility_parameters, T)""",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 30]
                }
            ]
        },
        {
            "id": "3.2.7",
            "question_template": "Reformulate the optimization model to guarantee that either the product with the index {product_1} or the product with index {product_2} is selected for the assortments, but not both.",
            "answer_template": """from gurobipy import Model, GRB, quicksum


def apv(prices, attraction_values, visibility_parameters, T):
    # Number of products
    n_products = len(prices)

    # Create a new Gurobi model
    m = Model("apv")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables: whether product i is in the assortment S_t for customer t
    x = m.addVars(T, n_products, vtype=GRB.BINARY, name="x")

    # New variable for the inverse of the denominator in the objective function
    y = m.addVars(T, name="y")

    # Objective function: Maximize total expected revenue
    # Non-linear term replaced by y[t]
    revenue = quicksum(prices[i] * attraction_values[i] * x[t, i] * y[t]
                       for t in range(T) for i in range(n_products))    
    m.setObjective(revenue, GRB.MAXIMIZE)

    # Constraints defining y[t] as the inverse of the sum in the denominator (to make it solvable by Gurobi)
    for t in range(T):
        m.addConstr(y[t] * (1 + quicksum(attraction_values[j] * x[t, j] for j in range(n_products))) == 1, "inverse_denominator")

    # Visibility constraints: each product i must be shown to at least visibility_parameters[i] customers
    for i in range(n_products):
        m.addConstr(quicksum(x[t, i] for t in range(T))
                    >= visibility_parameters[i], "visibility_constraint")
        
    # Exclusive products constraint: at most one of the products in the set must be selected
    for t in range(T):
        m.addConstr(x[t, {product_1}] + x[t, {product_2}] == 1, )

    # Solve the model
    m.setParam('NonConvex', 2)
    m.optimize()

    # Result handling
    if m.status == GRB.OPTIMAL:
        solution_x = m.getAttr('X', x)
        selected_items = [
            [i for i in range(n_products) if solution_x[t, i] > 0.5] for t in range(T)]
        objective_value = round(m.objVal)
    else:
        print("No optimal solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
prices = [20, 15, 40, 25, 50]  # Prices of products
attraction_values = [0.7, 0.8, 0.6, 0.9, 0.5]  # Attraction values for products
visibility_parameters = [2, 3, 1, 2, 2] # Minimum number of customers to show each product
T = 10  # Number of customers

# Running the model
selected_items, objective_value = apv(prices, attraction_values, visibility_parameters, T)""",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 30]
                }
            ]
        },
        {
            "id": "3.2.8",
            "question_template": "Reformulate the optimization model to double the expected revenue of the product with the index {product_1}",
            "answer_template": """from gurobipy import Model, GRB, quicksum


def apv(prices, attraction_values, visibility_parameters, T):
    # Number of products
    n_products = len(prices)

    # Create a new Gurobi model
    m = Model("apv")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables: whether product i is in the assortment S_t for customer t
    x = m.addVars(T, n_products, vtype=GRB.BINARY, name="x")

    # New variable for the inverse of the denominator in the objective function
    y = m.addVars(T, name="y")

    # Objective function: Maximize total expected revenue
    # Non-linear term replaced by y[t]
    revenue = quicksum(prices[i] * attraction_values[i] * x[t, i] * y[t]
                   for t in range(T) for i in range(n_products)) \
          + quicksum(prices[{product_1}] * attraction_values[{product_1}] * x[t, {product_1}] * y[t]
                     for t in range(T))
 
    m.setObjective(revenue, GRB.MAXIMIZE)

    # Constraints defining y[t] as the inverse of the sum in the denominator (to make it solvable by Gurobi)
    for t in range(T):
        m.addConstr(y[t] * (1 + quicksum(attraction_values[j] * x[t, j] for j in range(n_products))) == 1, "inverse_denominator")

    # Visibility constraints: each product i must be shown to at least visibility_parameters[i] customers
    for i in range(n_products):
        m.addConstr(quicksum(x[t, i] for t in range(T))
                    >= visibility_parameters[i], "visibility_constraint")

    # Solve the model
    m.setParam('NonConvex', 2)
    m.optimize()

    # Result handling
    if m.status == GRB.OPTIMAL:
        solution_x = m.getAttr('X', x)
        selected_items = [
            [i for i in range(n_products) if solution_x[t, i] > 0.5] for t in range(T)]
        objective_value = round(m.objVal)
    else:
        print("No optimal solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
prices = [20, 15, 40, 25, 50]  # Prices of products
attraction_values = [0.7, 0.8, 0.6, 0.9, 0.5]  # Attraction values for products
visibility_parameters = [2, 3, 1, 2, 2] # Minimum number of customers to show each product
T = 10  # Number of customers

# Running the model
selected_items, objective_value = apv(prices, attraction_values, visibility_parameters, T)""",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 30]
                }
            ]
        },
        {
            "id": "3.2.9",
            "question_template": "Reformulate the optimization model to incorporate a synergy between the products with indices {product_1} and {product_2}. When both are selected, a revenue of {add_revenue} is added.",
            "answer_template": """from gurobipy import Model, GRB, quicksum


def apv(prices, attraction_values, visibility_parameters, T):
    # Number of products
    n_products = len(prices)

    # Create a new Gurobi model
    m = Model("apv")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables: whether product i is in the assortment S_t for customer t
    x = m.addVars(T, n_products, vtype=GRB.BINARY, name="x")

    # New variable for the inverse of the denominator in the objective function
    y = m.addVars(T, name="y")

    # Objective function: Maximize total expected revenue, including synergy between products
    synergy_revenue = quicksum({add_revenue} * x[t, {product_1}] * x[t, {product_2}] for t in range(T))

    revenue = quicksum(prices[i] * attraction_values[i] * x[t, i] * y[t]
                   for t in range(T) for i in range(n_products)) + synergy_revenue
    m.setObjective(revenue, GRB.MAXIMIZE)

    # Constraints defining y[t] as the inverse of the sum in the denominator (to make it solvable by Gurobi)
    for t in range(T):
        m.addConstr(y[t] * (1 + quicksum(attraction_values[j] * x[t, j] for j in range(n_products))) == 1, "inverse_denominator")

    # Visibility constraints: each product i must be shown to at least visibility_parameters[i] customers
    for i in range(n_products):
        m.addConstr(quicksum(x[t, i] for t in range(T))
                    >= visibility_parameters[i], "visibility_constraint")

    # Solve the model
    m.setParam('NonConvex', 2)
    m.optimize()

    # Result handling
    if m.status == GRB.OPTIMAL:
        solution_x = m.getAttr('X', x)
        selected_items = [
            [i for i in range(n_products) if solution_x[t, i] > 0.5] for t in range(T)]
        objective_value = round(m.objVal)
    else:
        print("No optimal solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
prices = [20, 15, 40, 25, 50]  # Prices of products
attraction_values = [0.7, 0.8, 0.6, 0.9, 0.5]  # Attraction values for products
visibility_parameters = [2, 3, 1, 2, 2] # Minimum number of customers to show each product
T = 10  # Number of customers

# Running the model
selected_items, objective_value = apv(prices, attraction_values, visibility_parameters, T)""",
            "variables": [
                {
                    "name": "W",
                    "type": "int",
                    "range": [2, 30]
                }
            ]
        },
        {
            "id": "3.2.10",
            "question_template": "Reformulate the objective function to reflect the impact of a discount strategy, where the products with the indices {product_1} and {product_2} are offered at a discount of {discount_factor} times the original price",
            "answer_template": """from gurobipy import Model, GRB, quicksum


def apv(prices, attraction_values, visibility_parameters, T):
    # Number of products
    n_products = len(prices)

    # Create a new Gurobi model
    m = Model("apv")

    # Seed for reproducibility
    m.setParam('Seed', 1234)

    # Decision variables: whether product i is in the assortment S_t for customer t
    x = m.addVars(T, n_products, vtype=GRB.BINARY, name="x")

    # New variable for the inverse of the denominator in the objective function
    y = m.addVars(T, name="y")

    # Objective function: Maximize total expected revenue
    # Non-linear term replaced by y[t]
    revenue = quicksum(({discount_factor} * prices[i] if i in [{product_1}, {product_2}] else prices[i]) * attraction_values[i] * x[t, i] * y[t]
                   for t in range(T) for i in range(n_products))
 
    m.setObjective(revenue, GRB.MAXIMIZE)

    # Constraints defining y[t] as the inverse of the sum in the denominator (to make it solvable by Gurobi)
    for t in range(T):
        m.addConstr(y[t] * (1 + quicksum(attraction_values[j] * x[t, j] for j in range(n_products))) == 1, "inverse_denominator")

    # Visibility constraints: each product i must be shown to at least visibility_parameters[i] customers
    for i in range(n_products):
        m.addConstr(quicksum(x[t, i] for t in range(T))
                    >= visibility_parameters[i], "visibility_constraint")

    # Solve the model
    m.setParam('NonConvex', 2)
    m.optimize()

    # Result handling
    if m.status == GRB.OPTIMAL:
        solution_x = m.getAttr('X', x)
        selected_items = [
            [i for i in range(n_products) if solution_x[t, i] > 0.5] for t in range(T)]
        objective_value = round(m.objVal)
    else:
        print("No optimal solution found")
        selected_items = []
        objective_value = None

    return selected_items, objective_value


# Data
prices = [20, 15, 40, 25, 50]  # Prices of products
attraction_values = [0.7, 0.8, 0.6, 0.9, 0.5]  # Attraction values for products
visibility_parameters = [2, 3, 1, 2, 2] # Minimum number of customers to show each product
T = 10  # Number of customers

# Running the model
selected_items, objective_value = apv(prices, attraction_values, visibility_parameters, T)""",
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
