from sage.all import *
import random as rd
import numpy as np
import sympy as spy
import datetime as dt
import base64

def imply(p,q):
    return int(not p or q)

def iff(p,q):
    return int(imply(p,q) and imply(q,p))

def xor(p,q):
    return int((p or q) and not(p and q))

def tablify2(formula):
    formula=str(formula)
    p,q = var("p,q")
    code="def f(p,q): return %s" % formula
    exec(code)
    tabla = []
    cabecera = ["p", "q", formula]
    tabla.append(cabecera)
    for p in [True, False]:
        for q in [True, False]:
            renglon = [int(p), int(q), int(f(p,q))]
            tabla.append(renglon)
    show(table(tabla))
    
def tablify3(formula):
    formula=str(formula)
    p,q,r = var("p,q,r")
    code="def f(p,q,r): return %s" % formula
    exec(code)
    tabla = []
    cabecera = ["p", "q", "r", formula]
    tabla.append(cabecera)
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                renglon = [int(p), int(q), int(r), int(f(p,q,r))]
                tabla.append(renglon)
    show(table(tabla))
    
def tablify4(formula, importa=""):
    formula=str(formula)
    p,q,r,s = var("p,q,r,s")
    code="%s" % importa
    exec(code)
    code="def f(p,q,r,s): return %s" % formula
    exec(code)
    tabla = []
    cabecera = ["p", "q", "r", "s", formula]
    tabla.append(cabecera)
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                for s in [True, False]:
                    renglon = [int(p), int(q), int(r), int(s), int(f(p,q,r,s))]
                    tabla.append(renglon)
    show(table(tabla))

def urel(B):
    B = FiniteEnumeratedSet(B)
    U = []
    for x in B:
        for y in B:
            U.append([x,y])
    return U

def diag(B):
    B=FiniteEnumeratedSet(B)
    D=[]
    for x in B:
        D.append([x,x])
    return D

def reflexive(R,B):
    D = diag(B)
    for x in D:
        if not(x in R):
            return False
    return True

def symmetric(R):
    for par in R:
        x=par[0]; y=par[1]
        if not([y,x] in R):
            return False
    return True

def antisymmetric(R):
    for par in R:
        x=par[0]; y=par[1]
        if not(x==y) and ([y,x] in R):
            return False
    return True

def transitive(R):
    for par in R:
        for otro in R:
            if par[1]==otro[0]:
                if not([par[0], otro[1]] in R):
                    return False
    return True

def RelGen(A, B=True):
    #print B
    if B==True:
        B=copy(A)
    #print B
    A = FiniteEnumeratedSet(A)#; print A
    A = list(A)
    B = FiniteEnumeratedSet(B)#; print A
    B = list(B)
    AxB = []
    for x in A:
        for y in B:
            AxB.append([x,y])
    return list(powerset(AxB))#; print len(Rels)

def RelClassifier(A):
    equiv=[]
    order=[]
    milista=[]
    Rels = RelGen(A)
    #print Rels
    for R in Rels:
        #print R
        if reflexive(R, A) and transitive(R):
            if symmetric(R):
                equiv.append(R)
                milista.append(R)
            if antisymmetric(R):
                anexo = True
                for par in R:
                    if par[0]>par[1]:
                        anexo=False
                        break
                if anexo:
                    order.append(R)
                    if not(R in milista):
                        milista.append(R)
    return equiv, order, milista

def RelAnalyser(A):
    Rels = RelGen(A)
    mitabla=[["Relation", "Reflexive", "Symmetric", "Antisymmetric", "Transitive"]]
    for R in Rels:
        renglon=[R, reflexive(R, A), symmetric(R), antisymmetric(R), transitive(R)]
        mitabla.append(renglon)
    return mitabla

def SingletonsGen(B):
    lista = []
    for b in B:
        lista.append([b])
    return lista

def ImagesGen(B, N, test=False):
    k=1; l=len(B)
    X = SingletonsGen(B)#; print "X=",X    
    #X=[]
    #for i in range(l**N):
    #    X.append([])
    Y = []
    while k < N:
        for x in X:
            for b in B:
                y=copy(x)#; print x
                y.append(b)#; print y
                Y.append(y)
        X=copy(Y)
        Y=[]
        k+=1
        if test: print "ImageGen: step "+str(k)+" X="+str(X)
    return X

def FunGen(A,B, test=False):
    N=len(A)
    Ims=ImagesGen(B,N, test)
    Funs = []
    for im in Ims:
        fun = []
        for k,a in enumerate(A):
            fun.append([a,im[k]])
        if test: print "fun= "+str(fun)
        Funs.append(fun)
    return Funs

def oneone(fun):
    for k, pair in enumerate(fun):
        x=pair[0]
        y=pair[1]
        for i in range(k):
            xx = fun[i][0]
            yy = fun[i][1]
            if y==yy:
                return False
    return True

def image(fun):
    lista=[]
    for pair in fun:
        y = pair[1]
        lista.append(y)
    return list(Set(lista))

def onto(fun, B):
    if Set(image(fun))==Set(B):
        return True
    else:
        return False

def invertible(fun, B):
    if oneone(fun) and onto(fun, B):
        return True
    else:
        return False

def FunAnalyser(Funs, B):    
    mitabla=[["Function", "1:1", "Onto", "Invertible"]]
    for fun in Funs:
        renglon=[fun, oneone(fun), onto(fun,B), invertible(fun, B)]
        mitabla.append(renglon)
    return mitabla

def toSet(rel):
    relx=[]
    for x in rel:
        y=(x[0],x[1])
        relx.append(y)
    return Set(relx)

def grafica(formula, autoname=True, name="", foldername="temp", x0=0, y0=0, R=1, micolor="blue", npoints=200):
    #s = str(formula)
    code ="""x=var("x")"""; exec(code)
    code ="""f = (%s).function(x)""" % formula
    exec(code)
    
    M=max([f(x) for x in np.linspace(x0-R,x0+R, npoints)])
    m=max([f(x) for x in np.linspace(x0-R,x0+R, npoints)])
    
    titulo="\'$"+latex(f)+"$\'"
    print titulo
    code="""graf = plot(f, (x,x0-R,x0+R), ymin = y0-R, ymax = M, color=micolor, 
    title=r%s)""" % titulo
    print code
    exec(code)
    
    name=str(name)
    if not(name==""):
        autoname=False
    if autoname==True:
        tiempo=str(dt.datetime.now()) 
        filename="IMG-"+tiempo+".png"    
    else:
        filename="IMG-"+str(name)+".png"    
    if not os.path.isdir(foldername):
        os.makedirs(foldername)
    filenamext = os.path.join(foldername, filename)
    nombre=str(filename)
    nombrext=str(filenamext)
    graf.save(nombrext)
    #graf.show()
    with open(nombrext, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        #grafcod.append(str(encoded_string))
    return str(encoded_string)
