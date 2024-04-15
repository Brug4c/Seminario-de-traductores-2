import lexical
import sintactic

text = ""
archivo = open("example.txt",mode="r")
while(True):
    line = archivo.readline()
    if not line:
        break
    text = text + line
archivo.close()
print(text)
elements = lexical.analizador(text)
tree = sintactic.analizador(elements)

variables = []
functions = []
tree_2 = tree
if (tree):
    arbol = tree.Definiciones
    while(arbol):                   
        definicion = arbol.Definicion
        
        defvar = None
        try:
            defvar = definicion.DefVar
        except AttributeError:
            pass
        if(defvar):
            tipo = defvar.tipo
            while(defvar):
                variables.append({'id':defvar.identificador,'tipo':tipo,'valor':None,'contexto':"None"})
                try:
                    defvar = defvar.ListaVar.extra
                except AttributeError:
                    defvar = defvar.ListaVar


        deffun = None
        try:
            deffun = definicion.DefFunc
        except AttributeError:
            pass
        if(deffun):
            funcion = deffun.identificador
            functions.append({'id':deffun.identificador,'tipo':deffun.tipo})
            try:
                param = deffun.Parametros.extra     
            except AttributeError:
                param = deffun.Parametros
            while(param):
                variables.append({'id':param.identificador,'tipo':param.tipo,'valor':None,'contexto':funcion})
                try:
                    param = param.ListaParam.extra
                except AttributeError:
                    param = param.ListaParam
            bloc = deffun.BloqFunc
            try:
                bloc = bloc.DefLocales.extra        
            except AttributeError:
                bloc = bloc.DefLocales
            while(bloc):
                try:
                    defvar = bloc.DefLocal.DefVar     
                except AttributeError:
                    defvar = None
                if(defvar):
                    tipo = defvar.tipo
                    while(defvar):
                        variables.append({'id':defvar.identificador,'tipo':tipo,'contexto':funcion,'valor':None})
                        try:
                            defvar = defvar.ListaVar.extra
                        except AttributeError:
                            defvar = defvar.ListaVar

                try:
                    bloc = bloc.DefLocales.extra
                except AttributeError:
                    bloc = bloc.DefLocales


        try:
            arbol = arbol.Definiciones.extra
        except AttributeError:
            arbol = arbol.Definiciones


if(tree_2):
    arbol_2 = tree_2.Definiciones
    while(arbol_2):                   
        definicion = arbol_2.Definicion
        

        deffun = None
        try:
            deffun = definicion.DefFunc
        except AttributeError:
            pass
        if(deffun):
            funcion = deffun.identificador
            bloc = deffun.BloqFunc
            try:
                bloc = bloc.DefLocales.extra       
            except AttributeError:
                bloc = bloc.DefLocales
            while(bloc):
                try:
                    sentence = bloc.DefLocal.Sentencia.identificador     
                    sentence = bloc.DefLocal.Sentencia
                except AttributeError:
                    sentence = None
                if(sentence):
                    id = sentence.identificador
                    
                    try:
                        expresion = sentence.Expresion.Termino
                    except AttributeError:
                        expresion = None
                    if(expresion):
                        for a in variables:
                            if(a["id"]==id):
                                try:
                                    a["valor"] = expresion.entero
                                except AttributeError:
                                    try:
                                        a["valor"] = expresion.real
                                    except AttributeError:
                                        try:
                                            a["valor"] = expresion.cadena
                                        except AttributeError:
                                            for b in variables:
                                                if(b["id"]==expresion.identificador):
                                                    a["valor"] = b["valor"]


                    try:
                        expresion = sentence.Expresion.Expresion2
                        expresion = sentence.Expresion
                    except AttributeError:
                        expresion = None
                    if(expresion):
                        a=0
                        b=0
                        try:
                            a = expresion.Expresion.Termino.entero
                        except AttributeError:
                            try:
                                a = expresion.Expresion.Termino.real
                            except AttributeError:
                                try:
                                    a = expresion.Expresion.Termino.cadena
                                except AttributeError:
                                    for b in variables:
                                        if(b["id"]==expresion.Expresion.Termino.identificador):
                                            a = b["valor"]
                        try:
                            b = expresion.Expresion2.Termino.entero
                        except AttributeError:
                            try:
                                b = expresion.Expresion2.Termino.real
                            except AttributeError:
                                try:
                                    b = expresion.Expresion2.Termino.cadena
                                except AttributeError:
                                    for c in variables:
                                        if(c["id"]==expresion.Expresion2.Termino.identificador):
                                            b = c["valor"]

                        try:
                            operacion = expresion.opSuma
                        except AttributeError:
                            try:
                                operacion = expresion.opMul
                            except AttributeError:
                                operacion = None
                        if(operacion == "+"):
                            for i in variables:
                                if(i["id"] == id):
                                    i["valor"]=a+b
                        elif(operacion == "-"):
                            for i in variables:
                                if(i["id"] == id):
                                    i["valor"]=a-b
                        elif(operacion == "*"):
                            for i in variables:
                                if(i["id"] == id):
                                    i["valor"]=int(a)*int(b)
                        elif(operacion == "/"):
                            for i in variables:
                                if(i["id"] == id):
                                    i["valor"]=a/b
                    

                try:
                    bloc = bloc.DefLocales.extra
                except AttributeError:
                    bloc = bloc.DefLocales
        

        try:
            arbol_2 = arbol_2.Definiciones.extra
        except AttributeError:
            arbol_2 = arbol_2.Definiciones

print("\n")
print("FUNCIONES")
print("ID","\t","TIPO")
for a in functions:
    print(a["id"],"\t",a["tipo"])

print("\n")
print("VARIABLES")
print("ID","\t\t","TIPO","\t\t","CONTEXTO","\t","VALOR")
for a in variables:
    print(a["id"],"\t\t",a["tipo"],"\t\t",a["contexto"],"\t\t",a["valor"])