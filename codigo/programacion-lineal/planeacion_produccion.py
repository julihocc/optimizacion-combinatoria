from ortools.linear_solver import pywraplp

"""Linear programming sample."""
# Instantiate a Glop solver, naming it LinearExample.
solver = pywraplp.Solver.CreateSolver('GLOP')

# Create the two variables and let them take on any non-negative value.
x = solver.NumVar(0, solver.infinity(), 'x')
y = solver.NumVar(0, solver.infinity(), 'y')
z = solver.NumVar(0, solver.infinity(), 'z')

print('Number of variables =', solver.NumVariables())

# Constraint 0:
solver.Add(3*x+5*y+4*z<=540)

# Constraint 1:
solver.Add(6*x+y+3*z<=480)

print('Number of constraints =', solver.NumConstraints())

# Objective function: 3x + 4y.
solver.Maximize(5*x+3.5*y+4.5*z)

# Solve the system.
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('Objective value =', solver.Objective().Value())
    print('x =', x.solution_value())
    print('y =', y.solution_value())
    print('z =', z.solution_value())
else:
    print('The problem does not have an optimal solution.')

print('\nAdvanced usage:')
print('Problem solved in %f milliseconds' % solver.wall_time())
print('Problem solved in %d iterations' % solver.iterations())
