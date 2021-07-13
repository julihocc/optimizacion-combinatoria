#!/usr/bin/env python
# coding: utf-8

# # Problema Resuelto 3
# ## Problemas de mezcla de productos
# 
# Una compañía fabrica tres productos: crema corporal, crema facial y crema para bebés. Los tres productos
# comparten ingredientes en su elaboración: mezcla base, aceite de almendras, vitamina E y manteca
# de karité. En la siguiente tabla se presenta información acerca de los porcentajes de composición de cada
# uno de los tres productos:
# 
# | . | Mezcla base | Aceite de Almendras | Vitamina E | Manteca de karité |
# |---|-------------|---------------------|------------|-------------------|
# |Crema Corporal| 90% | 4% | 1% | 5% |
# |Crema facial  | 85% | 8% | 2.5% | 4.5% |
# |Crema para bebé | 80% | 10% | - | 10% |

# Cada día, la compañía cuenta con 500 litros de la mezcla base, 50 litros de aceite de almendras, 5 litros
# de vitamina E y 30 litros de manteca de karité. Adicionalmente, se tiene la siguiente información sobre
# costos y precios de venta.

# | Ingrediente | Costo por litro |
# |-------------|-----------------|
# |Mezcla base  | \$20 |
# |Aceite de almedras | \$500 |
# |Vitamina E | \$1500 |
# |Manteca de karité | \$200 |

# | Producto | Precio de venta (\$/L) |
# |----------|------------------------|
# |Crema corporal | \$80 |
# |Crema facial | \$120 |
# |Crema para bebé | \$100 |

# La demanda diaria de la crema corporal es de 200 litros; de la crema facial, 150 litros; y de la crema para
# bebé, de 250 litros. Por políticas de la empresa, se deben fabricar al menos 50 litros de crema facial.
# ¿Cuánto de cada producto deberá producir la compañía para maximizar su utilidad?

"""
Índice: producto
0: crema corporal
1: crema facial
2: crema para bebé
"""

from ortools.linear_solver import pywraplp
from sympy import Matrix

solver = pywraplp.Solver.CreateSolver("GLOP")

insumos = ["mezcla", "aceite", "vitamina", "manteca"]
productos = ["corporal", "facial", "bebe"]

"""
Restricciones para productos
° Restricción para la demanda de crema corporal: 0<= x0 <= 200.
° Restricción para la demanda de crema facial: 50<= x1 <= 150.
° Restricción para la demanda de crema para bebé: 0 <= x2 <= 250.
"""

restricciones_productos = dict(
    zip(productos, [[0,200], [50,150], [0,250]])
)

inf = solver.infinity()
x = dict()
for producto, restriccion in restricciones_productos.items():
    a, b = restriccion
    x[producto] = solver.NumVar(a,b,producto)

"""
Beneficio = Ingreso - Costo
"""
pct_values = [
    [0.90, 0.04, 0.01, 0.05],
    [0.85, 0.08, 0.025, 0.045],
    [0.80, 0.10, 0.00, 0.10]
]

pct = dict(
    [(producto,
        dict(
            zip(insumos, renglon)
            )
      )
     for producto, renglon in zip(productos, pct_values)]
)

print(pct)



"""
Cm: costo marginal por litro
"""
Cm = Matrix([
    20, 500, 1500, 200
])

# """
# costo productos = T(costo ingredientes)
# """
C = Matrix(pct_values)*Cm
print("C <-",C)

"""
I : ingresos
"""
I = Matrix([
    80, 120, 100
])
print("I <-",I)

"""
R: Ingresos
"""
R = dict(
    zip(productos, (I-C))
)
print("R <- ", R)

solver.Maximize(
    sum(R[tag]*x[tag] for tag in productos)
)


"""
Restricciones para insumos
° Restricción para la mezcla base: 0.9x0 + 0.85x1 + 0.8x2 <= 500.
° Restricción para el aceite de almendras: 0.04x0 + 0.08x1 + 0.1x2 <= 50.
° Restricción para la vitamina E: 0.01x0 + 0.025x1 <= 5.
° Restricción para la manteca de karité: 0.05x0 + 0.045x1 + 0.1x2 <= 30.
"""
restricciones_insumos = dict(zip(insumos, [500, 50, 5, 30]))

for insumo in insumos:
    #insumo_total = 0
    #for producto in productos:
        #insumo_total = insumo_total + pct[producto][insumo]*x[producto]
    solver.Add(
        sum(
            pct[producto][insumo]*x[producto] for producto in productos
        )<=restricciones_insumos[insumo]
    )



# Resolvemos el sistema.
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

