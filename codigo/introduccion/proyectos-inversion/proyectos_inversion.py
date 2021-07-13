#!/usr/bin/env python
# coding: utf-8

# ## Problema de proyectos de inversión
#
# Imaginemos que ocupamos el puesto de coordinador de proyectos dentro de una empresa. El gerente
# general de dicha empresa ha destinado 100,000 pesos para invertir en los proyectos que generen beneficios
# económicos a esta. Existen tres proyectos en los que se puede invertir. ¿En cuál(es) proyecto(s)
# debería invertir la empresa para obtener los máximos beneficios económicos?
#
# Se tiene la siguiente información sobre los proyectos:
#
# |Nombre|Costo de Inversión|Benefició económico|
# |:----:|:----------------:|:------------------|
# |Proyecto A| \$50,000 | \$80,000 |
# |Proyecto B| \$70,000 | \$90,000 |
# |Proyecto C| \$25,000 | \$30,000 |

from ortools.linear_solver import pywraplp

# SCIP(Solving Constraint Integer Programs)
solver = pywraplp.Solver.CreateSolver('SCIP')
x = {}
tags = ["A", "B", "C"]

for tag in tags:
    x[tag] = solver.IntVar(0, 1, tag)

cost = {'A': 50_000, 'B': 70_000, 'C': 25_000}
utility = {'A': 80_000, 'B': 90_000, 'C': 30_000}
solver.Add(sum(cost[tag] * x[tag] for tag in tags) <= 100000)
solver.Maximize(sum(utility[tag] * x[tag] for tag in tags))

# Solve the system.
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('Solución:')
    print('Valor objetivo =', solver.Objective().Value())
    for k, v in x.items():
        print("Variable: {}, valor:{} ".format(k, v.solution_value()))

else:
    print('EL problema no tiene solución óptima.')

print('\nUso avanzado:')
print('Problema resuelto en %f milisegundos' % solver.wall_time())
print('Problema resuelto en %d iteraciones' % solver.iterations())

"""
Solución:
Valor objetivo = 120000.0
Varible: A, valor:0.0 
Varible: B, valor:1.0 
Varible: C, valor:1.0 

Uso avanzado:
Problema resuelto en 111.000000 milisegundos
Problema resuelto en 0 iteraciones
"""