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

#definiciones
def isName(s, i):
    res = False
    d= 0
    if i == 0:
        if len(s)>=1:
            if s[0].isalpha():
                for c in s:
                    if c.isalpha() or c.isnumeric():
                        d+=1
                
    if i==1:
        s = s[:-1]
        if len(s)>=1:
            if s[0].isalpha():
                for c in s:
                    if c.isalpha()or c.isnumeric():
                        d+=1
    if d== len(s):
        res = True         
    return res
#print(isName("loquesea ", 0))
