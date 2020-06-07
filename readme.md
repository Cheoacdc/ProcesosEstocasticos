# Proyecto Final Procesos Estocásticos

Este proyecto fue desarrollado para acreditar la materia de procesos estocásticos de la carrera de Matemáticas Aplicadas y Computación, impartida por la FES Acatlán en el periodo 2020-2. 

# Descripción

El programa es una aplicación de consola, desarrollado en Python 3.7. Su funcionalidad es el cálculo de la mejor política de decisión para un Problema Markoviano de Decisión (PMD).

# Instalación
## Para poder correr el código desde su máquina

Para descargar el contenido de este repositorio a su computadora, lo único que tiene que hacer es clonar el repositorio. Puede dar click en el botón verde en la esquina superior derecha que dice *Clone or download*, o puede correr el siguiente comando desde la consola.

```sh
$ git clone https://github.com/Cheoacdc/ProcesosEstocasticos.git
```

Sin embargo, dado que el proyecto está desarrollado usando [Python](https://www.python.org/downloads/) 3.7, usted debe tener al menos Python 3.0 si desea correr y/o modificar el código desde su máquina. Por favor, haga click en el link e instale la versión estable más reciente, si es que no la tiene en su máquina.

### Dependencias adicionales

Este proyecto require tanto [numpy](https://numpy.org/) como [scipy](https://www.scipy.org/) para poder funcionar. Para instalar ambos módulos, puede correr los siguientes comandos en su consola:

```sh
$ pip install numpy scipy
```

#### Creando un virtual environment

Tambien es posible utilizar el siguiente comando para crear un ambiente virtual (virtual environment), y sólo instalar los módulos en dicho ambiente. Primero debe instalar pipenv de la siguiente manera:

```sh
$ pip install pipenv
```

Posteriormente, el siguiente comando instalará aqullos módulos que están especificados en los archivos [Pipfile](./Pipfile) y [Pipfile.lock](./Pipfile.lock).

```sh
$ pipenv sync
```

Esta es la manera recomendada, ya que asegura que las versiones sean exactamente las mismas a las que se utiliazaron durante el desrrollo de este proyecto.