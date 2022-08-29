def arreglarFormato(f):
    i = 0                           # "PROG GORP"
    while i< len(f):
        f[i]= f[i].strip("\n")
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

def inicioEsVar(f):
    VAR = False
    if len(f)>=1:
        if len(f[1])>=4:
            if f[1][0] == 'V' and f[1][1] == 'A' and f[1][2] == 'R' and f[1][3] == ' ':
                VAR = True
    return VAR

def llavesAperturaPresentes(lineNumber, f):
    presente=True
    if f[lineNumber][-1] != '{' and f[lineNumber+1][0]!='{':
        presente = False
    if f[lineNumber][-1] == '{' and f[lineNumber+1][0]=='{':
        presente = False
    return presente

def llavesCerrarPresentes(lineNumber, f):
    presente=True
    if f[lineNumber][0] != '}' and f[lineNumber-1][-1]!='}':
        presente = False
    if f[lineNumber][0] == '}' and f[lineNumber-1][-1]=='}':
        presente= False
    return presente

def PROCs(f):    #Retorna lista de listas. No revisa ni nombre ni parametros en la signatura.
                #Revisa que existan las respectivas parejas de PROC-CORP y llaves de abrir y cerrar
                #Si no se cumple retorna False

    i=0
    inicioRangoActual = 0
    finRangoActual = 0
    rangoActual = []
    PROCs = []
    lineNumber= 0

    if len(f)<=2:
        return False

    for line in f:
        if "PROC " in line:
            if (i!=0) or (llavesAperturaPresentes(lineNumber, f)==False):
                return False
            i+=1
            inicioRangoActual = lineNumber

        if "CORP" in line:
            if (i!=1) or (llavesCerrarPresentes(lineNumber, f)==False):
                return False
            if '}' in line:
                lList= line.split('}')
                if ((lList[1].strip()) != "CORP"):
                    return False
                
            i-=1
            finRangoActual = lineNumber+1
            rangoActual = f[inicioRangoActual:finRangoActual]
            PROCs.append(rangoActual)

        lineNumber +=1
    if i!=0:
        PROCs= False
    return PROCs #PROCs es tambien llamado listaPrevia 

def revisarEstructura(listaPrevia): 
    
    for PROC in listaPrevia:
        if len(PROC[0])>=8:
            signatura = PROC[0][5:]
            if ' ' in signatura:
                lista=signatura.split(" ",1)
                if isName(lista[0],0,5) and lista[1][0]=="(":
                    if lista[1].count('(')==1:
                        lista[1]=lista[1].strip('(')
                        listaparametros= lista[1].split(",")
                        p=0
                        c=0
                        if lista[1].count(')')==1:
                            if listaparametros[-1][-1]=='{':
                                listaparametros[-1]=listaparametros[-1].rstrip('{')
                            while p < len(listaparametros):
                                listaparametros[p]= listaparametros[p].strip()
                                if isName(listaparametros[p],len(listaparametros), p+1):                                    
                                    c+=1 
                                p+=1
                            if c==p:
                                return True
                           
        return False

#definiciones
def isParameter(listaParametros):
    i=0
    for parametro in listaParametros:
        if type(parametro)==int:
            i+=1

def isName(s, i,j):
    res = False
    d= 0
    if i ==j:
        if ';' in s or (')' in s):
            s = s[:-1]
        else:
            return False
        
    if len(s)>=1:
        if s[0].isalpha():
            for c in s:
                if c.isalpha() or c.isnumeric():
                    d+=1              

    if d== len(s):
        res = True         
    return res
