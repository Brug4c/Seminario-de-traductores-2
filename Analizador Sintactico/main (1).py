import lenguaje
from pila import Pila
from lenguajeEP import EP

pila = Pila()
matriz = [[2,-1,-1,1],
          [-1,-1,-2,-1],
          [-1,3,-4,-1],
          [2,-1,-1,4],
          [-1,-1,-3,-1]]

estado = 0
texto = input("Introduce el texto a analizar: ")
elementos = lenguaje.analizador(texto)
e = False
accepted = False
recibido = -1
pila.push(0)
a = 0

while not accepted and a < len(elementos):
    print(pila)
    input()
    estado = pila.top()

    if elementos[a]['token'] == "id":
        recibido = 0
    elif elementos[a]['token'] == "OpSuma":
        recibido = 1
    elif elementos[a]['token'] == "pesos":
        recibido = 2

    if isinstance(estado, EP):
        recibido = 3
        e_cont = pila.pop()
        e = True
        estado = pila.top()

    accion = matriz[estado][recibido]
    
    if accion == -1:    
        print("Cadena no aceptada")
        accepted = True
    elif e:            
        pila.push(e_cont)
        pila.push(accion)
        e = False
        a+=1
    elif accion >= 0:   
        pila.push(elementos[a]['lexema'])
        pila.push(accion)
        a+=1
    elif accion == -2:  
        print("Cadena aceptada")
        pila.pop()
        b = pila.pop()
        print(b)
        accepted = True
    elif accion == -3: 
        c = EP("E")
        pila.pop()
        c.E = pila.pop()
        pila.pop()
        c.mas = pila.pop()
        pila.pop()
        c.id = pila.pop()
        pila.push(c)
    elif accion == -4:  
        c = EP("E")
        pila.pop() 
        c.id = pila.pop() 
        pila.push(c)
