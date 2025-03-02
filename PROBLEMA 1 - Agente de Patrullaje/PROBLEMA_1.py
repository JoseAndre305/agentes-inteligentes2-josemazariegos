import random
import time

class AgentePatrullaje:
    def __init__(self, ruta):
        self.ruta = ruta
        self.posicion = 0
        self.direccion = 1  # 1 para adelante, -1 para atrás

    def detectar_obstaculo(self):
        """Simula la detección de obstáculos con una probabilidad del 20%."""
        return random.random() < 0.2

    def cambiar_direccion(self):
        """Cambia la dirección del agente aleatoriamente."""
        self.direccion = random.choice([1, -1])

    def patrullar(self):
        """Inicia el patrullaje a lo largo de la ruta definida."""
        while True:
            if self.detectar_obstaculo():
                print(f"¡Obstáculo detectado en posición {self.posicion}! Cambiando dirección.")
                self.cambiar_direccion()
            else:
                self.posicion += self.direccion
                # Verifica los límites y ajusta la posición y dirección según sea necesario
                if self.posicion >= len(self.ruta):
                    self.posicion = len(self.ruta) - 1
                    self.direccion = -1
                elif self.posicion < 0:
                    self.posicion = 0
                    self.direccion = 1
                
                print(f"Agente en posición: {self.ruta[self.posicion]}")
            
            time.sleep(1)

# Definir la ruta de patrullaje
ruta = [f"Punto {i}" for i in range(10)]

# Crear una instancia del AgentePatrullaje y comenzar a patrullar
agente = AgentePatrullaje(ruta)
agente.patrullar()