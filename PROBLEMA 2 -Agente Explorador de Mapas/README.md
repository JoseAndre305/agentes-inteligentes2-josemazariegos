1. Importaciones: Se importan las bibliotecas random para la generación de números aleatorios y time para manejar pausas en la ejecución.

2. Clase AgenteExplorador: Esta clase representa un agente que explora un mapa bidimensional.

    __init__: Inicializa el agente con un mapa de dimensiones filas x columnas, una posición inicial en la esquina superior izquierda, un conjunto de posiciones visitadas, y una lista de direcciones posibles para moverse (derecha, abajo, izquierda, arriba).

    mover: Este método determina los movimientos válidos desde la posición actual del agente. Si hay movimientos válidos, elige uno aleatoriamente y actualiza la posición del agente, además de marcar la nueva posición como visitada.
    
    explorar: Este método inicia el proceso de exploración. Agrega la posición inicial a las visitadas y continúa moviendo al agente hasta que todas las posiciones del mapa hayan sido visitadas. Imprime la posición actual del agente en cada paso y finaliza con un mensaje de completado.
3. Instanciación y Ejecución: Se crea una instancia de AgenteExplorador con un mapa de 5x5 y se inicia el proceso de exploración.