# Problema de proyectos de inversión

Imaginemos que ocupamos el puesto de coordinador de proyectos dentro de una empresa. El gerente
general de dicha empresa ha destinado 100 000 pesos para invertir en los proyectos que generen beneficios
económicos a esta. Existen tres proyectos en los que se puede invertir. ¿En cuál(es) proyecto(s)
debería invertir la empresa para obtener los máximos beneficios económicos?
Se tiene la siguiente información sobre los proyectos:

|Nombre|Costo de Inversión|Benefició económico|
|:----:|:----------------:|:------------------|
|Proyecto A| \$50,000 | \$80,000 |
|Proyecto B| \$70,000 | \$90,000 |
|Proyecto C| \$25,000 | \$30,000 |


```python
program = MixedIntegerLinearProgram()
inversion = program.new_variable(binary=True)
program.show()
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-1-72f09e5d33ad> in <module>
    ----> 1 program = MixedIntegerLinearProgram()
          2 inversion = program.new_variable(binary=True)
          3 program.show()
          4 


    NameError: name 'MixedIntegerLinearProgram' is not defined



```python
cost = {'A':50_000, 'B':70_000, 'C':25_000}
utility = {'A': 80_000, 'B':90_000, 'C':30_000}
```


```python
program.add_constraint(cost['A']*inversion['A']+cost['B']*inversion['B']+cost['C']*inversion['C'] <= 100_000)
program.show()
```


```python
program.set_objective(utility['A']*inversion['A']+utility['B']*inversion['B']+utility['C']*inversion['C'] )
program.show()
```


```python
program.solve()
```


```python
program.get_values(inversion)
```
