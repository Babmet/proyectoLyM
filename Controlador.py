import Modelo as m
import copy



def abrirArchivo(path):
    pathToFile= path
    file = open(pathToFile, 'r' )
    f =file.readlines()
    i = 0                           # "PROG GORP"
    while i< len(f):
        f[i]= f[i].strip("\n")
        f[i]= f[i].strip(" ")
        i+=1
    i=0
    j =len(f)
    while i<j+1:
        if "" in f:
            f.remove("")
        if "\n" in f:
            f.remove("\n")
        i+=1

    
        
    return f

def initProg(f):
    PROG = True
    if (f[0] != "PROG") or (f[-1] != "GORP") or (f.count('PROG')>1) or (f.count('GORP')>1):
        PROG = False
    return PROG

def initVar(f):
    variables= {}
    VAR = m.inicioEsVar(f)
    k=0
    i =0
    if VAR and len(f[1])>=5:
        l = f[1][4:]                   #l es el string de la 2da linea sin "VAR "
        tokenList = l.split(",")       #tolenList es una lista de posibles candidatos a ser names
        
        while k< len(tokenList):
            tokenList[k]=tokenList[k].strip()
            k+=1
        if '' in tokenList:
            tokenList.remove('')
        if (len(tokenList)==0) or (tokenList[0]==";"):
            return False
        if tokenList[-1][-1]==';':
            i=len(tokenList)
            j=1
            for token in tokenList:
                if m.isName(token, i,j) is False:
                    return (False, token)          #NO se declararon variables correctamente
                variables.update({token:''})
                j+=1
            return (True, variables)                   #Se declararon correctamente
    return False

def Procedures(f):
    listaPrevia = m.PROCs(f)
    if (listaPrevia == False) or (m.revisarEstructura(listaPrevia)[0] != True):
        return (False, False)
    return (listaPrevia,m.revisarEstructura(listaPrevia)[1])

           

