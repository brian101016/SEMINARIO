# SEMINARIO

Repositorio para guardar toda la información y archivos de la clase de Seminario de Programación.

## Proyecto final

Dentro de la carpeta del mismo nombre, podemos encontrar el código para el proyecto final, el cual trata de una aplicación CRUD utilizando **Django**.

La aplicación se basa en administrar una base de datos mediante PostreSQL sobre los registros y libros de sacramentos parroquiales básicos.

### Instalar

1. Una vez tengamos clonado el repositorio, entramos a la carpeta contenedora (SEMINARIO).
2. Dentro de la carpeta, abrimos una consola (cmd o PowerShell).
   - NOTA: Se puede usar la consola de **VSCode** pero deberá ser una consola de **cmd**.
3. En la consola, accedan a la carpeta de `proyecto_final` (con el comando `cd`).
4. Verifiquen que tienen Python instalado usando: `python --version`
5. Actualicen el `pip` por si acaso, usando el comando: `python -m pip install --upgrade pip`
6. Una vez que tengan la versión más nueva de **pip** (en mi caso es la 24.0), **dentro de la carpeta proyecto_final** necesitan crear el entorno virtual usando: `python -m venv venv`
7. Cuando hagan el **venv**, lo activan usando el comando: `venv\Scripts\activate`
8. Si en la consola les aparece al inicio de la línea un `(venv)` enconces significa que está activado el **venv**.
9. Ahora que tienen el **venv** activado, van a instalar **Django** dentro de ahí mismo usando: `pip install django`
10. Después de que se instale ya estarán listos para correr el servidor.

### Ejecutar el servidor

1. Necesitan acceder mediante consola a la carpeta "SEMINARIO/proyecto_final".
2. Dentro de ahí se supone que hay un archivo llamado `manage.py`.
3. Deben activar el **venv** en caso de que no lo tengan activado usando: `venv\Scripts\activate`
4. Ahora, ingresan el comando `python manage.py runserver`
5. Si el servidor se iniciará dentro de la consola, cuando quieran apagarlo pueden pulsar `CTRL+C` o cerrar la consola.
6. Si quieren ver la aplicación, pueden acceder en cualquier navegador con la URL `localhost:8000/`

### Django

Por si no conocen como funciona Django les explico brevemente:

1. Es un **framework** y es como el equivalente de _React_ para JS, pero ahora para Python.

2. Así como _React_ se necesita ejecutar desde un servidor, Django también necesita lo mismo.

3. Cuando trabajamos con _React_ usamos un bundler llamado **webpack** que se encargaba juntar todos los archivos en un directorio
   y de administrar las librerías, dependencias y todo eso. Pues en **Django** también se usa algo similar gracias al **venv** (que es un entorno virtual donde ocurre toda la magia de montar el servidor y prenderlo).

4. En _React_ nosotros omitíamos las librerías de **node_modules** para que no se metieran al GitHub, pues en Django se omite el **venv** que también tiene información de ese estilo
   (y sobre todo, se puede autogenerar e instalar siempre que lo necesitemos).

5. Así como en _React_ trabajamos con **componentes**, en Django se trabaja con **apps** (que es el equivalente).

6. Django es muy popular al igual que _React_, por lo que hay mucha documentación y tutoriales, y van a encontrar bastantes paralelismos entre ellos (como que **NodeJS -> npm** ; **Python -> pip**).

## Equipo (grupo 001)

1. Laprada Coronado Juan Pablo
2. López Bojórquez Orlando
3. Rivera López Pablo
4. Vasquez Fernandez Jesus Ruben
5. Woolfolk Cerecer Brian
