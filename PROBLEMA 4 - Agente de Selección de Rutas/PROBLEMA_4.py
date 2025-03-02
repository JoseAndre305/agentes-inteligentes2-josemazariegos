from collections import deque

class AgenteNavegacion:
    def __init__(self, laberinto, inicio):
        # Inicializa el laberinto, la posición de inicio y la meta
        self.laberinto = laberinto
        self.inicio = inicio
        self.meta = (len(laberinto) - 1, len(laberinto[0]) - 1)  # Definir la meta como la esquina inferior derecha
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])
        self.direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Movimientos: derecha, abajo, izquierda, arriba

    def buscar_ruta(self):
        """Busca una ruta desde el inicio hasta la meta utilizando búsqueda en anchura."""
        cola = deque([(self.inicio, [self.inicio])])  # Cola para almacenar posiciones y rutas
        visitados = set()  # Conjunto para almacenar posiciones visitadas
        visitados.add(self.inicio)
        
        while cola:
            (x, y), ruta = cola.popleft()  # Extrae la posición y la ruta actual
            
            if (x, y) == self.meta:  # Verifica si se ha alcanzado la meta
                return ruta
            
            for dx, dy in self.direcciones:
                nx, ny = x + dx, y + dy  # Calcula la nueva posición
                
                # Verifica si la nueva posición es válida y no ha sido visitada
                if (0 <= nx < self.filas and 0 <= ny < self.columnas and
                    self.laberinto[nx][ny] == 0 and (nx, ny) not in visitados):
                    cola.append(((nx, ny), ruta + [(nx, ny)]))  # Agrega la nueva posición y ruta a la cola
                    visitados.add((nx, ny))  # Marca la nueva posición como visitada
        
        return []  # Retorna una lista vacía si no se encuentra ruta

    def navegar(self):
        """Inicia el proceso de navegación y muestra la ruta encontrada."""
        ruta = self.buscar_ruta()
        if ruta:
            print("Ruta encontrada:")
            for paso in ruta:
                print(paso)
        else:
            print("No se encontró una ruta a la meta.")

# Definición del laberinto y posición de inicio
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

inicio = (0, 0)  # Posición de inicio

# Crear una instancia del AgenteNavegacion y mostrar la salida
agente = AgenteNavegacion(laberinto, inicio)
print(f"La salida a buscar está en la posición: {agente.meta}")  # Mostrar la meta
agente.navegar()