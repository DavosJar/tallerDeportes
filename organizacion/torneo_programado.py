from info.modelo import *

class Jugador(Persona):
    def __init__(self, nombre, edad, posicion, dorsal, estaSancionado):
        super().__init__(nombre, edad)
        self.posicion = posicion
        self.dorsal = dorsal
        self.estaSancionado = estaSancionado

    def __str__(self):
        sancionado_str = "Sí" if self.estaSancionado else "No"
        return (f"Nombre: {self.nombre}, Edad: {self.edad}, Posición: {self.posicion}, "
                f"Dorsal: {self.dorsal}, Sancionado: {sancionado_str}")

class EstadisticaJugador:
    def __init__(self, partidos_jugados, goles, asistencias, tarjetas_acumuladas):
        self.partidos_jugados = partidos_jugados
        self.goles = goles
        self.asistencias = asistencias
        self.tarjetas_acumuladas = tarjetas_acumuladas

    def __str__(self):
        return (f"Partidos jugados: {self.partidos_jugados}, Goles: {self.goles}, "
                f"Asistencias: {self.asistencias}, Tarjetas acumuladas: {self.tarjetas_acumuladas}")

class Equipo:
    def __init__(self, nombre, nacionalidad, jugadores):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.jugadores = jugadores
        self.puntos = 0  # Atributo de puntos

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Nacionalidad: {self.nacionalidad}, Puntos: {self.puntos}"
class Inscripcion:
    def __init__(self, equipo, campeonato, fecha):
        self.equipo = equipo
        self.campeonato = campeonato
        self.fecha = fecha
    
    def __str__(self):
        return (f"Equipo: {self.equipo.nombre}, Campeonato: {self.campeonato.nombre}, Fecha: {self.fecha}")

class CampeonatoProgramado(Campeonato):
    def __init__(self, nombre, fecha_inicio, fecha_fin, tipo, categoria, equipos_inscritos=None, estado=None):
        super().__init__(nombre, fecha_inicio, fecha_fin, tipo, categoria)
        self.equipos_inscritos = equipos_inscritos if equipos_inscritos is not None else []
        self.estado = estado

    def agregar_equipo(self, equipo):
        super().agregar_equipo(equipo)
        self.equipos_inscritos.append(equipo)

    def __str__(self):
        return (f"Nombre: {self.nombre}, Fecha de inicio: {self.fecha_inicio}, Fecha de fin: {self.fecha_fin}, "
                f"Tipo: {self.tipo.name}, Categoría: {self.categoria.name}, "
                f"Equipos inscritos: {len(self.equipos_inscritos)}, Estado: {self.estado.name}")

class Grupo:
    def __init__(self, nombre, equipos=None):
        self.nombre = nombre
        self.equipos = equipos if equipos is not None else []
    
    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)
    
    def __str__(self):
        equipos_str = ", ".join(equipo.nombre for equipo in self.equipos)
        return f"Nombre: {self.nombre}, Equipos: [{equipos_str}]"

class Estado(Enum):
    PROGRAMADO = 1
    JUGADO = 2
    SUSPENDIDO = 3
    CANCELADO = 4
    APLAZADO = 5