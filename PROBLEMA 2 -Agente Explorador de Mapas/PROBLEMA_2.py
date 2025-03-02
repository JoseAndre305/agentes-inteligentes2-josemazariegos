import random
import time

class AgenteExplorador:
    def __init__(self, filas, columnas):
        # Inicializa el mapa, la posición inicial, los lugares visitados y las dimensiones
        self.mapa = [[0 for _ in range(columnas)] for _ in range(filas)]
        self.posicion = [0, 0]
        self.visitados = set()
        self.filas = filas
        self.columnas = columnas
        self.direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Movimientos: derecha, abajo, izquierda, arriba

    def mover(self):
        """Mueve al agente a una nueva posición válida."""
        movimientos_validos = []
        for dx, dy in self.direcciones:
            nueva_pos = [self.posicion[0] + dx, self.posicion[1] + dy]
            
            # Verifica si la nueva posición es válida y no ha sido visitada
            if (0 <= nueva_pos[0] < self.filas and 0 <= nueva_pos[1] < self.columnas
                and tuple(nueva_pos) not in self.visitados):
                movimientos_validos.append(nueva_pos)
        
        # Si hay movimientos válidos, elige uno aleatoriamente
        if movimientos_validos:
            self.posicion = random.choice(movimientos_validos)
            self.visitados.add(tuple(self.posicion))

    def explorar(self):
        """Inicia el proceso de exploración del mapa."""
        self.visitados.add(tuple(self.posicion))
        
        # Continúa explorando hasta que todas las posiciones hayan sido visitadas
        while len(self.visitados) < self.filas * self.columnas:
            self.mover()
            print(f"Agente explorando: {self.posicion}")
            time.sleep(0.5)
        
        print("¡Exploración completada! Todas las áreas han sido visitadas.")

# Crear un entorno de 5x5
explorador = AgenteExplorador(5, 5)
explorador.explorar()