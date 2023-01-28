# Tarea 2: DCComando Espacial :school_satchel:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

#### Ventana de Inicio: 4 pts (4%)
#### Ventana de Ranking: 5 pts (5%)
#### Ventana principal: 7 pts (7%)
#### Ventana de juego: 14 pts (13%)
#### Ventana de post-nivel: 5 pts (5%)
#### Mecánicas de juego: 47 pts (45%)
##### ✅ Arma <explicacion\> El arma se mueve de manera fluida, con una animación y funcionamiento correcto. Para el disparo hice utilización de la tecla F.
##### 🟠 Aliens y Escenario de Juego <explicacion\> En mi implementación, el movimiento de los aliens con repecto al nivel anterior funciona correctamente por lo que entiendo, pero cuando el vector adquiere un valor negativo va más rápido, algo que desconozco la razón de por que pasa. Tampoco definí la restricción para que no aparezcan uno sobre otro.
##### 🟠 Fin de Nivel <explicacion\> Para terminar el nivel la condicion de tiempo, aunque la barra de tiempo funcione correctamente, el tiempo restante no tuve tiempo de arreglarlo y se resta continuamente.
##### ✅ Fin del juego <explicacion\> La ventana post-juego entrega todos los resultados de manera correcta y al salir del juego se almacena el puntaje en el archivo de puntajes.
#### Cheatcodes: 8 pts (8%)
##### ✅ Pausa <explicacion\>
##### ✅ O + V+ N + I <explicacion\> Este cheat se valida y bloquea el descuento de balas, manteniendo el puntaje de esas balas pero permitiendo realizar disparos infinitos.
##### ✅  C + I + A <explicacion\> Este cheat se valida y salta el nivel directamente, otorgando el puntaje acumulado hasta la ejecución del cheat.
#### General: 14 pts (13%)
##### ✅ Modularización <explicacion\> Modularicé los archivos de código por categoría o funcionamiento. Para mantener debajo de 400 lineas dividí clases de la lógica del juego, con lógica mira y lógica aliens.
##### ✅ Modelación <explicacion\> Modelé siguiendo la estructura Frontend-Backend utilizando señales conectadas en main.py, trabajando con modelación orientada a objetos.
##### ✅ Archivos  <explicacion\> Utilicé todos los archivos pedidos de correcta manera.
##### ✅ Parametros.py <explicacion\> Definí multiples parametros siguiendo el formato para generar un rapido y facil acceso a ellos.
#### Bonus: 10 décimas máximo
##### ✅ Risa Dog <explicacion\> La risa se reproduce siempre que terminator dog tiene un alien en la mano, dependiendo del escenario, el sprite es apropiado.
##### ❌ Estrella <explicacion\> No fue implementado.
##### ❌ Disparos extra <explicacion\> No fue implementado.
##### ❌ Bomba <explicacion\> No fue implementado.
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```archivo.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```main.py``` en ```Carpeta T2```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint, choice```
2. ```PyQt5```: ```QtWidgets, QtCore, QtGui, QtMultimedia``` (debe instalarse)
3. ```sys```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```lectura```: Contiene a ```escribir```, ```leer```.
2. ```parametros```: Contiene los parametros a utilizar.
3. ```ventana_inicio```: Contiene a ```VentanaInicio```.
4. ```ventana_ranking```: Contiene a ```VentanaRanking```.
5. ```ventana_principal```: Contiene a ```VentanaPrincipal```.
6. ```logica_principal```: Contiene a ```LogicaPrincipal```.
7. ```ventana_juego```: Contiene a ```VentanaJuego```.
8. ```logica_juego```: Contiene a ```LogicaJuego```.
9. ```logica_mira```: Contiene a ```Mira```.
10. ```logica_alien```: Contiene a ```Alien```.
11. ```ventana_post_juego```: Contiene a ```VentanaPostJuego```.
12. ```logica_post_juego```: Contiene a ```LogicaPostJuego```.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Interpreté que pasar al siguiente nivel era pasar al siguiente escenario y por ende solo hay tres niveles./a> 


## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
