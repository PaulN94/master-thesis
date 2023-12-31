from gurobipy import Model, GRB, quicksum


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
prices = [20, 15, 40, 25, 50, 73, 52, 73, 60, 71] # Prices of products
attraction_values = [0.7, 0.8, 0.6, 0.9, 0.5, 0.6, 0.9, 0.6, 0.8, 0.7] # Attraction values for products
visibility_parameters = [2, 3, 1, 2, 2, 3, 1, 2, 3, 1] # Minimum number of customers to show each product
T = 10  # Number of customers

# Running the model
selected_items, objective_value = apv(prices, attraction_values, visibility_parameters, T)