
def analizador(entrada):
    salida = []

    reservadas = {'if', 'while', 'return', 'else'}
    tipo = {'int', 'float', 'void'}
    relacionales = {'<', '<=', '>', '>=', '!=', '=='}
    aritmeticos = {'+', '-'}
    opMul = { '*', '/'}
    otros_simbolos = {'(', ')', '{', '}', ';', ','}
    asignacion = {'='}


    i = 0
    longitud = len(entrada)

    while i < longitud:
        posicion = entrada[i]

        if posicion.isalpha() or posicion == '_':
            
            caracter = posicion
            i += 1
            while i < longitud and (entrada[i].isalnum() or entrada[i] == '_'):
                caracter += entrada[i]
                i += 1

            if caracter in reservadas:
                salida.append(('Palabra_Reservada', caracter))
            elif caracter in tipo:
                salida.append(('Tipo', caracter, '4'))
            else:
                salida.append(('Identificador', caracter, '0'))

        elif posicion.isdigit():
            
            caracter = posicion
            i += 1
            while i < longitud and (entrada[i].isdigit() or entrada[i] == '.'):
                caracter += entrada[i]
                i += 1

            if '.' in caracter:
                salida.append(('Real', float(caracter), '2'))
            else:
                salida.append(('Entero', int(caracter), '1'))

        elif posicion in aritmeticos:
            salida.append(('Operador_Suma', posicion,'5'))
            i += 1
        elif posicion in opMul:
            salida.append(('Operador_Multiplicacion', posicion,'6'))
            i += 1

        elif posicion in relacionales:
            caracter = posicion
            i += 1
            if i < longitud and entrada[i] == '=':
                caracter += '='
                i += 1
            salida.append(('Operador_Relacional', caracter, '7'))

        elif posicion in otros_simbolos:
            salida.append(('Otro_Simbolo', posicion))
            i += 1

        elif posicion in asignacion:
            salida.append(('Operador_Asignacion', posicion, '18'))
            i += 1

        elif posicion.isspace():
            i += 1

        elif posicion == '&' or posicion == '|':
            caracter = posicion
            i += 1
            if i < longitud and entrada[i] == posicion:
                caracter += entrada[i]
                i += 1
                salida.append(('Operador_Logico', caracter))
            else:
                print(f"Error: Operador lógico no reconocido '{caracter}'")
        
        elif posicion == '!':
            caracter = posicion
            i += 1
            salida.append(('Operador_Logico', caracter))

        else:
            print(f"Error: Caracter no reconocido '{posicion}'")
            i += 1

    return salida


entrada = input("Texto a analizar: ")
salida = analizador(entrada)

print(salida)
