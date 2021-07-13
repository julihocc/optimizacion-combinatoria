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

# In[1]:


"""
Índice: producto
0: crema corporal
1: crema facial
2: crema para bebé
"""

programa = MixedIntegerLinearProgram()
x = programa.new_variable() # cantidades en litros
programa.show()


# In[2]:


"""
Beneficio = Ingreso - Costo

T: insumos -> productos
"""
T  = matrix([
    [0.90, 0.04, 0.01, 0.05],
    [0.85, 0.08, 0.025, 0.045],
    [0.80, 0.10, 0.00, 0.10]
])
show(T)


# In[3]:


"""
Cm: costo marginal por litro
"""
Cm = matrix([
    20, 500, 1500, 200
]).transpose()
show(Cm)


# In[4]:


"""
costo productos = T(costo ingredientes)
"""
C = T*Cm
show(C)


# In[5]:


"""
I : ingresos
"""
I = matrix([
    80, 120, 100
]).transpose()
show(I)


# In[6]:


"""
R: Ingresos
"""
R = (I-C).list()
show(R)

programa.set_objective(
    R[0]*x[0]+R[1]*x[1]+R[2]*x[2]
)
programa.show()
# In[7]:


Rx = 0
for i in [0,1,2]:
    Rx = Rx+R[i]*x[i]

programa.set_objective(Rx)
programa.show()


# In[8]:


"""
Restricciones para insumos
° Restricción para la mezcla base: 0.9x0 + 0.85x1 + 0.8x2 ≤ 500.
° Restricción para el aceite de almendras: 0.04x0 + 0.08x1 + 0.1x2 ≤ 50.
° Restricción para la vitamina E: 0.01x0 + 0.025x1 ≤ 5.
° Restricción para la manteca de karité: 0.05x0 + 0.045x1 + 0.1x2 ≤ 30.
"""
r_insumos = [500, 50, 5, 30]


# In[9]:


for col in [0,1,2,3]:
    insumo = 0
    for row in [0,1,2]:
        insumo = insumo + T[row, col]*x[row]
    restriccion = insumo <=r_insumos[col]
    programa.add_constraint(restriccion)
    
programa.show()


# In[10]:


"""
Restricciones para productos
° Restricción para la demanda de crema corporal: 0<= x0 ≤ 200.
° Restricción para la demanda de crema facial: 50<= x1 ≤ 150.
° Restricción para la demanda de crema para bebé: 0 <= x2 ≤ 250.
"""

r_productos = [[0,200], [50,150], [0,250]]

for i in [0,1,2]:
    oferta = r_productos[i][0] <= x[i] <= r_productos[i][1]
    programa.add_constraint(oferta)
    
programa.show()


# In[11]:


programa.solve()


# In[12]:


programa.get_values(x)

