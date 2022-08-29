import Controlador as c

f = c.abrirArchivo("C:\\Users\\Administrator\\Documents\\Universidad\\4\\lym\\1\\prueba.txt")
if c.initProg(f): #verifica que se declare un nuevo programa correctamente. Devuelve boolean
    res, variables = c.initVar(f)     #verifica que se declaren variables correctamente. Devuelve  (boolean, {variable1:'', variable2:''...})
    if res:
        PROCs, diccionarioParametros = c.Procedures(f) 
                                #si no esta bien hecha la declaracion retorna (False, False)
                                #Retorna una tupla:
                                #el primer elemento es unalista de listas. La lista grande contiene listas con las lineas de las definiciones de procedimientos
                                #EJ: [['PROC putCB (c, b)', '{', 'drop (c);', 'free (b);', 'walk (n)', '}', 'CORP'], ['PROC ', '{', 'while ( canWalk (north ,1) ) do { walk (north ,1) } od', '}', 'CORP']]
                                #el segundo elemento es un diccionario de la forma {nombreprocedimiento1: ['parametro1','parametro2']}
        
        
