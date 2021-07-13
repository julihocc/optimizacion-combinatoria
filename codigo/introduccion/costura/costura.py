#!/usr/bin/env python
# coding: utf-8

# ## Fabricación de ropa
# 
# Una costurera fabrica y vende faldas y pantalones de mezclilla, para lo cual cada semana compra un
# rollo de 50 metros de mezclilla. Para hacer un pantalón requiere 2 metros de tela, mientras que para
# una falda, 1.5 metros.
# 
# Por lo general, ella trabaja ocho horas diarias, de lunes a viernes. Para hacer un pantalón requiere
# tres horas, mientras que hacer una falda le toma una. Un pantalón le genera 80 pesos de ganancia,
# mientras que al vender una falda gana 50 pesos.
# 
# Construir un modelo matemático que permita maximizar la ganancia semanal de la costurera, considerando
# que todo producto que fabrique puede venderlo.

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver('SCIP')
infinity = solver.infinity()
n={}
tags = ["pantalon", "falda"]
for tag in tags:
    n[tag] = solver.IntVar(0, infinity, tag)

material = {'pantalon': 2, 'falda': 1.5}
tiempo = {'pantalon': 3, 'falda': 1}
ganancia = {'pantalon': 80, 'falda': 50}

solver.Add(
    material['pantalon']*n['pantalon']+ material['falda']*n['falda']<=50
)

solver.Add(
    tiempo['pantalon']*n['pantalon']+tiempo['falda']*n['falda']<=40
)

solver.Maximize(
    ganancia['pantalon']*n['pantalon']+ganancia['falda']*n['falda']
)

# Resolvemos el sistema.
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('Solución:')
    print('Valor objetivo =', solver.Objective().Value())
    for k, v in n.items():
        print("Variable: {}, valor:{} ".format(k, v.solution_value()))

else:
    print('EL problema no tiene solución óptima.')

print('\nUso avanzado:')
print('Problema resuelto en %f milisegundos' % solver.wall_time())
print('Problema resuelto en %d iteraciones' % solver.iterations())




