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

# In[1]:


program = MixedIntegerLinearProgram()
inversion = program.new_variable(binary=True)
program.show()


# In[2]:


cost = {'A':50_000, 'B':70_000, 'C':25_000}
utility = {'A': 80_000, 'B':90_000, 'C':30_000}


# In[3]:


program.add_constraint(cost['A']*inversion['A']+cost['B']*inversion['B']+cost['C']*inversion['C'] <= 100_000)
program.show()


# In[4]:


program.set_objective(utility['A']*inversion['A']+utility['B']*inversion['B']+utility['C']*inversion['C'] )
program.show()


# In[5]:


program.solve()


# In[6]:


program.get_values(inversion)

