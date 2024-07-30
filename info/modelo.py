from datetime import datetime
from enum import Enum

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = ""
        self.nacionalidad = ""
    
    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento
    
    def set_nacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad
    
    def __str__(self):
        return (f"Nombre: {self.nombre}, Edad: {self.edad}, Fecha de nacimiento: {self.fecha_nacimiento}, "
                f"Nacionalidad: {self.nacionalidad}")

class Arbitro(Persona):
    def __init__(self, nombre, edad, experiencia):
        super().__init__(nombre, edad)
        self.experiencia = experiencia
    
    def set_experiencia(self, experiencia):
        self.experiencia = experiencia
        
    def __str__(self):
        return (f"Nombre: {self.nombre}, Edad: {self.edad}, Fecha de nacimiento: {self.fecha_nacimiento}, "
                f"Nacionalidad: {self.nacionalidad}, Experiencia: {self.experiencia}")

class Tipo(Enum):
    LIGA = 1
    COPA = 2
    AMISTOSO = 3

class Categoria(Enum):
    MASCULINO = 1
    FEMENINO = 2

class Campeonato:
    def __init__(self, nombre, fecha_inicio, fecha_fin, tipo, categoria):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tipo = tipo
        self.categoria = categoria
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)
    
    def generar_partidos(self):
        pass
    
    def presentar_estadisticas(self):
        pass

class Partido:
    def __init__(self, equipo_local, equipo_visitante, fecha, hora, lugar, arbitro):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha
        self.hora = hora
        self.lugar = lugar
        self.arbitro = arbitro
        self.resultado = None

    def asignar_resultado(self, goles_local, goles_visitante):
        self.resultado = Resultado(goles_local, goles_visitante)
        
        if goles_local > goles_visitante:
            self.equipo_local.puntos += 3  
        elif goles_visitante > goles_local:
            self.equipo_visitante.puntos += 3  
        else:
            self.equipo_local.puntos += 1  
            self.equipo_visitante.puntos += 1  
class Resultado:
    def __init__(self, goles_local, goles_visitante):
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante

    def obtener_resultado(self):
        return f"Resultado: {self.goles_local} - {self.goles_visitante}"

class EstadisticaCampeonato:
    def __init__(self, equipos):
        self.equipos = equipos

    def obtener_tabla_posiciones(self):
        # Ordena los equipos por puntos en orden descendente
        sorted_equipos = sorted(self.equipos, key=lambda equipo: equipo.puntos, reverse=True)
        # Asigna posiciones a cada equipo
        tabla = [(i + 1, equipo) for i, equipo in enumerate(sorted_equipos)]
        return tabla