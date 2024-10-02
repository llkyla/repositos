#####################
from mip import *
#####################

# Model
m1 = Model()
m2 = Model(sense=MAXIMIZE, solver_name=CBC)

#   lb: variable lower bound, default 0.0
#   ub: variable upper bound, default infinity
#   obj: coefficient of this variable in the objective function, default 0
#   var_type: values which the variable may hold, including CONTINUOUS, BINARY, or INTEGER
#   column: constraints where this variable will appear, necessary only when constraints 
#           are already created in the model and a new variable will be created
#   name: allows storing of a variable to a certain name - particularly useful if you plan 
#         to save the model

x = m1.add_var()

# integer decision variable greater than 5
y = m1.add_var(lb=5.0, var_type=INTEGER)

# continuous decision variable called zCost ranging from -10 to 10
z = m1.add_var(name='zCost', var_type=CONTINUOUS, lb=-10, ub=10)