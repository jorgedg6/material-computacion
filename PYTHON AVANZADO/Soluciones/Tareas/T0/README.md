# Tarea 0: DCCorreos :school_satchel:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<Mi programa se mueve entre todos los menús requeridos y accede a todas las funciones correctamente. Si existe una falla particular no la he notado con mi debuggeo.>

### Cosas implementadas y no implementadas :white_check_mark: :x:


#### Menú de Inicio (18pts) (18%)
##### ✅ Requisitos <hola\>
##### ✅ Iniciar sesión <Hice una funcion en ```criptografia.py``` que me verifica la pertenencia de la tupla (usuario, contraseña) en el archivo usuarios.py leyendo el archivo mediante una funcion en lectura.py ordenandolos en tuplas. Esta función si es erróneo el input se retorna al usuario al menu de inicio y si es correcto avanzará al menú de usuario.\>
##### ✅ Ingresar como administrador <Hice una funcion en ```criptografia.py``` que verifica que la contraseña ingresada equivalga a la contraseña de ```parametros.py```. Si es correcto se avanza al usuario al menu de administrador y en caso contrario se le pregunta si quiere intentar nuevamente o no, en caso de sí querer se llamará a la función de verificación de manera recursiva, si no se vuelve al menu de inicio.\>
##### ✅ Registrar usuario <Hice una cadena de funciones recursivas en ```criptografia.py``` que verifican el nombre de usuario nuevo revisando que no esté siendo utilizado que comienza con la función ```verificar_nuevo_usuario```. Una vez se verifique la validez de los datos en ```lectura.py``` con la función ```agregar_usuario``` se inscribe al archivo.\>
##### ✅ Salir <Permití que el usuario pudiera cerrar el programa y el terminal.\>
#### Flujo del programa (31pts) (31%) 
##### ✅ Menú de Usuario <El menú de usuario hereda su nombre de usuario a través de funciones recursivas que permiten el flujo entre la creacion de encomiendas, el revisado del estado y creación de reclamos que se mueven entre los distintos modulos, explicitados en las anotaciones en el código.\>
##### ✅ Menú de Administrador <El menú de administrador mueve al usuario a través de sus opciones de manera recursiva a través de los módulos del programa como está descrito en las anotaciones del código.\>
#### Entidades 15pts (15%)
##### ✅ Usuarios <Diseñé funciones que leen y guardan los usuarios en ```lectura.py``` para que la verificación posteriormente los utilice en la función ```verificar_usuario``` y ```verificar_nuevo_usuario```\>
##### ✅ Encomiendas <Diseñé una cadena de funciones recursivas en ```manejo_encomiendas.py``` que permite al usuario crear encomiendas un atributo a la vez y comienza con ```nombre_encomienda``` y otra función ```actualizar_encomiendas``` que le permite al administrador mediante una función recursiva actualizar el estado de cada encomienda. Su escritura \>
##### ✅ Reclamos <Hice una función para crear un reclamo y una para visualizarlos en manejo_reclamos.py. La primera le permite al usuario definir un título y descripción a su reclamo el cual será inscrito en el archivo reclamos.csv por la función ```agregar_reclamo``` en ```lectura.py```. La segunda función permite al administrador circular los títulos del archivo ```reclamos.csv``` y recursivamente mantenerse dentro del visualizador o volver al menu de administrador.\>
#### Archivos: 15 pts (15%)
##### ✅ Manejo de Archivos <Modularicé todo el manejo de archivos y lo especialicé para cada uno en lectura.py, se abren y modifican de manera correcta.\>
#### General: 21 pts (21%)
##### ✅ Menús <Me movilicé correctamente entre los menús del programa manteniendo un orden en los prints y una estética útil para el usuario.\>
##### ✅ Parámetros <Importé y apliqué de manera correcta los parametros entregados en parametros.py en el flujo del programa.\>
##### ✅ Módulos <Creé un fluído y rápido acceso entre funciones de los modulos creados por mi.\>
##### ✅ PEP8 <Separé todos los argumentos dentro de funciones por comas con espaciado, mantuve menor a 100 caracteres todas las líneas de mi programa, utilicé snake_case y CamelCase apropiadamente, dejé separados los operadores matemáticos y modularicé mi programa para que ningún archivo tenga sobre 400 líneas.\>
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```encomiendas_usuarios.csv``` en ```Carpeta principal (Esta uploadeado pero lo especifico de igual manera)```



## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```Datetime```: ```today().strftime() / datetime```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```menus```: Contiene las funciones ```menu_inicio```, ```menu_usuario``` y ```menu_administrador```. Sus funciones son abrir y dar al usuario acceso a sus respectivos menus.
2. ```criptografia```: Contiene funciones que se encargan de verificar las contraseñas y usuarios en el programa.
3. ```manejo_encomiendas```: Contiene funciones que se encargan de crear y actualizar las encomiendas.
4. ```manejo_reclamos```: Contiene funciones que se encargan de crear y revisar los reclamos.
5. ```lectura```: Contiene funciones que se encargan de leer y editar los archivos de texto.


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Asumí que ningun usuario ha creado encomiendas hasta que se prueba el programa, debido a que no se posee información de quién realizó que encomienda de las que están contenidas en encomiendas.csv./a> 

-------



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://www.programiz.com/python-programming/datetime>: este me otorga la fecha actual en el formato requerido para la creación de encomiendas y está implementado en el archivo \<lectura.py> en las líneas \<38> y \<obtiene de un servidor la fecha del día de hoy y la hora en mi zona horaria>


## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
