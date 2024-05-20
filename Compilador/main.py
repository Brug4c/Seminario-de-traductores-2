import lexico
import sintactico
import semantico

#texto = input("Introduce el texto a analizar: ")
texto = ""
archivo = open(r"C:\Users\brand\Downloads\Compilador\Ejemplo1.txt", mode="r")
while(True):
    linea = archivo.readline()
    if not linea:
        break
    texto = texto + linea
archivo.close()
print(texto)
elementos = lexico.analizador(texto)
arbol = sintactico.analizador(elementos)
try:
    f = open("codigo.asm", "x")
    f.close()
except:
    pass
semantico.analizador(arbol)

