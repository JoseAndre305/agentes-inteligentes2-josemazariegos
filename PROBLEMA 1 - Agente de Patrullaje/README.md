1. Importaciones: Se importan las bibliotecas random para la generación de números aleatorios y time para manejar pausas en la ejecución.

2. Clase AgentePatrullaje: Esta clase representa un agente que patrulla a lo largo de un camino definido.

    __init__: Inicializa el agente con una ruta (ruta), una posición inicial (posicion), y una dirección inicial (direccion).

    detectar_obstaculo: Simula la detección de obstáculos con una probabilidad del 20%. Devuelve True si se detecta un obstáculo.

    cambiar_direccion: Cambia la dirección del agente aleatoriamente entre adelante y atrás.

    patrullar: Método principal que ejecuta el patrullaje. En un bucle infinito, el agente verifica si hay un obstáculo. Si lo hay, cambia de dirección; si no, avanza en la dirección actual y verifica los límites de la ruta.

3. Definición de la Ruta: Se crea una lista de puntos que representan la ruta de patrullaje.

4. Instanciación y Ejecución: Se crea una instancia de AgentePatrullaje con la ruta definida y se inicia el patrullaje.