1. Importación de Módulos:

    Se importa deque de la biblioteca collections para utilizar una cola que permite realizar operaciones de inserción y eliminación de manera eficiente.

2. Clase AgenteNavegacion:

    __init__: Inicializa el agente con el laberinto, la posición de inicio y define la meta como la esquina inferior derecha del laberinto. También establece las dimensiones del laberinto y las posibles direcciones de movimiento (derecha, abajo, izquierda, arriba).

3. Método buscar_ruta:

    Implementa un algoritmo de búsqueda en anchura (BFS) para encontrar una ruta desde la posición de inicio hasta la meta. Utiliza una cola para explorar las posiciones y un conjunto para llevar un registro de las posiciones visitadas.

    Si encuentra la meta, devuelve la ruta; si no, retorna una lista vacía.

4. Método navegar:

    Inicia el proceso de navegación llamando a buscar_ruta. Si se encuentra una ruta, la imprime; de lo contrario, informa que no se encontró una ruta.

5. Definición del Laberinto:

    Se define un laberinto como una lista de listas, donde 0 representa un espacio libre y 1 representa un obstáculo.

6. Instanciación y Ejecución:

    Se crea una instancia de AgenteNavegacion con el laberinto y la posición de inicio. Se imprime la posición de la salida (meta) y se inicia el proceso de navegación.