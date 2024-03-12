En este readme detallare los avances que llevo sobre el compilador, de momento con el analizador Lexico completo y con el analizador sintactico.

Primero detallare el analizador lexico:
El analizador lexico consta de una funcion que como su nombre lo indica analiza el texto ingresado en la consola, esto lo hace a forma de automata, esta funcion tiene distintos tipos de operadores para reconocer, los cuales se muestran a continuacion:
![image](https://github.com/Brug4c/Seminario-de-traductores-2/assets/157430737/4ba82ec7-ea27-436d-ac06-71bbf669a6a5)

A la vez que va analizando el texto lo va etiquetando y dandole un valor, ademas de guardandolo en una lista que se utilizara mas adelante en el analizador sintactico.

La forma en la cual trabaja el analizador lexico es a base de ifs y whiles, unos anidados dentro de otros.

Aqui unos ejemplos de entradas y salidas del analuzador lexico.

![image](https://github.com/Brug4c/Seminario-de-traductores-2/assets/157430737/635c91e9-f1e4-4d26-b5c5-d48b682aa278)
![image](https://github.com/Brug4c/Seminario-de-traductores-2/assets/157430737/fbe54905-5e91-4f3b-931f-77c1e8f4e4e3)

Ahora voy a explicar el analizador sintactico:
El analizador sintactico ya es un poco mas complejo en cuanto a la funcion y a la forma de programar, ya cuenta con archivos de cabecera, estos archivos de cabecera son la pila y el lenguaje.
Hasta este momento el analizador lexico y el analizador sintactico aun no estan conectados para que trabajen juntos.

Un ejemplo del analizador sintactco
