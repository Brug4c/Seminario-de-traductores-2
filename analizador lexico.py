import re

salida = []

def analizador(entrada):
    
    identificador = r'[a-zA-Z_]\w*'
    entero = r'[0-9]*'
    real = r'[0-9]*\.[0-9]*'
    #tipo = r'[int, float, void]'
    #opSuma = 
    

    patron = f'({identificador})|({real})|({entero})'

    coincidencias = re.findall(patron, entrada)


    for identificador, real, entero in coincidencias:
        if identificador:
            salida.append(('Identificador', identificador, '0'))
        elif entero: 
            salida.append(('Entero', int(entero), '1'))
        elif real:
            salida.append(('Real', float(real), '2'))
        
            
    return salida



entrada = input("Texto a analizar: ")
salida = analizador(entrada)


print(salida)
