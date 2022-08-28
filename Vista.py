import Controlador as c

f = c.abrirArchivo("C:\\Users\\Administrator\\Documents\\Universidad\\4\\lym\\1\\prueba.txt")
PROG = c.initProg(f) #verifica que se declare un nuevo programa correctamente. Devuelve boolean
res = c.initVar(f)     #verifica que se declaren variables correctamente. Devuelve boolean
print(res)
