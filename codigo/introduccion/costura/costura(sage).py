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

# In[1]:


programa = MixedIntegerLinearProgram()
n = programa.new_variable(nonnegative=True)
programa.show()


# In[2]:


material = {'pantalon': 2, 'falda': 1.5}
tiempo = {'pantalon': 3, 'falda': 1}
ganancia = {'pantalon': 80, 'falda': 50}


# In[3]:


programa.add_constraint(
    material['pantalon']*n['pantalon']+ material['falda']*n['falda']<=50
)
programa.show()


# In[4]:


programa.add_constraint(
    tiempo['pantalon']*n['pantalon']+tiempo['falda']*n['falda']<=40
)
programa.show()


# In[5]:


programa.set_objective(
    ganancia['pantalon']*n['pantalon']+ganancia['falda']*n['falda']
)
programa.show()


# In[6]:


programa.solve()


# In[7]:


programa.get_values(n)


# In[ ]:




