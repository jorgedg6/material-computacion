# Tarea X: Nombre de la tarea :school_satchel:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<El programa inicializa la conexion, envia informacion codificada y avanza a los usuarios hasta la ventana de espera, pudiendo pasar a la ventana de juego.>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

#### Networking: 23 pts (18%)
##### 🟠 Protocolo <explicacion\> Al recibir la informacion se sigue el protocolo preocupandose que todo el contenido llegue de manera correcta.
##### ✅ Correcto uso de sockets <explicacion\> Los sockets del cliente y el servidor se conectan y comunican de manera apropiada.
##### ✅ Conexión <explicacion\> La conexion se mantiene frente a la caida de algun cliente.
##### 🟠 Manejo de clientes <explicacion\> Al terminar la conexion de un cliente, el manejo del programa no elimina correctamente toda su informacion que se utiliza en la ventana de espera.

#### Arquitectura Cliente - Servidor: 31 pts (25%)
##### ✅ Roles <explicacion\> El rol de cliente y servidor estan claramente diferenciados, pudiendo ejecutarse desde terminales distintos.
##### ✅ Consistencia <explicacion\> Todos los mensajes se entregan del cliente al servidor correctamente, aquellos que fallan es por el codigo y flujo del programa por la parte del juego,  la base de comunicación es consistente.
##### 🟠 Logs <explicacion\> Se logea informacion de conexion y desconexion, sin la implementacion de mayor detalle.

#### Manejo de Bytes: 26 pts (21%)
##### ✅ Codificación <explicacion\> La codificacion del mensaje se realiza de acuerdo a las instrucciones de manera correcta.
##### ✅ Decodificación <explicacion\> La decodificacion del mensaje se realiza de acuerdo a las instrucciones y al protocolo de llegada de manera correcta.
##### 🟠 Encriptación <explicacion\> La encriptación la programé de manera correcta, a mi parecer, pero al no lograr la desencriptacion no lo conecte al flujo programa.
##### ❌ Desencriptación <explicacion\> No realizado.
##### 🟠 Integración <explicacion\> La comunicacion integra de manera parcial el protocolo de encriptacion/codificacion.


#### Interfaz: 23 pts (18%)
##### ✅ Ventana inicio <explicacion\> Defini la interfaz grafica de la ventana de inicio de manera correcta, permitiendo la verificacion del nombre de usuario.
##### ✅ Sala de Espera <explicacion\> Defini la interfaz grafica de la sala de espera de manera correcta, mostrando los nombres y colores de los usuarios.
##### 🟠 Sala de juego <explicacion\> Creé la interfaz de la sala de juego pero no implemente funcionalidades.
##### ❌ Ventana final <explicacion\> No realizado.


#### Reglas de DCCasillas: 18 pts (14%)
##### ❌ Inicio del juego <explicacion\> No realizado.
##### ❌ Ronda <explicacion\> No realizado.
##### ❌ Termino del juego <explicacion\> No realizado.


#### General: 4 pts (3%)
##### ✅ Parámetros (JSON) <explicacion\> Defini los parametros independientes de cliente y servidor en formato .json y accedí correctamente a estos.
#### Bonus: 5 décimas máximo
##### ❌ Cheatcode <explicacion\> No realizado.
##### ❌ Turnos con tiempo <explicacion\> No realizado.
##### ❌ Rebote <explicacion\> No realizado.

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py``` de las carpetas cliente y servidor.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```choice / randint```
2. ```PyQt5```: ```QtCore / QtGui / QtWidgets``` (debe instalarse)

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```servidor```: Contiene a ```Servidor```
2. ```ventana_inicio```: Contiene a ```VentanaInicio```
3. ```ventana_espera```: Contiene a ```VentanaEspera```
4. ```ventana_juego```: Contiene a ```VentanaJuego```
5. ```cliente/logica```: Contiene a ```Logica```
6. ```servidor/logica```: Contiene a ```Logica```

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. No realicé supuestos notables.

PD: Movi la ubicacion de los sprites dentro de la carpeta frontend para ordenar mi setup, la direccion relativa se puede evidenciar en el gitignore de la tarea.


-------