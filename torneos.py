from datetime import datetime
from info.modelo import Tipo, Categoria, Campeonato, Partido, Arbitro, EstadisticaCampeonato
from organizacion.torneo_programado import *

def main():
    # Crear jugadores
    jugadores_equipo_A = [Jugador(f"Jugador A{i+1}", 20 + i, "Delantero", i + 1, False) for i in range(15)]
    jugadores_equipo_B = [Jugador(f"Jugador B{i+1}", 20 + i, "Defensa", i + 1, False) for i in range(15)]
    
    # Crear equipos
    equipo_A = Equipo("Equipo A", "Nacionalidad A", jugadores_equipo_A)
    equipo_B = Equipo("Equipo B", "Nacionalidad B", jugadores_equipo_B)
    
    # Crear campeonato
    campeonato = CampeonatoProgramado("Campeonato 1", datetime(2024, 7, 1), datetime(2024, 12, 31), Tipo.LIGA, Categoria.MASCULINO, [], Estado.PROGRAMADO)
    campeonato.agregar_equipo(equipo_A)
    campeonato.agregar_equipo(equipo_B)
    
    # Crear partidos
    partido1 = Partido(equipo_A, equipo_B, datetime(2024, 7, 10), "15:00", "Estadio A", Arbitro("Arbitro 1", 35, "Alta"))
    partido2 = Partido(equipo_B, equipo_A, datetime(2024, 7, 20), "17:00", "Estadio B", Arbitro("Arbitro 2", 40, "Alta"))
    
    # Asignar resultados
    partido1.asignar_resultado(2, 2)  # Empate 2-2
    partido2.asignar_resultado(1, 0)  # Victoria de Equipo B
    
    # Imprimir resultados de los partidos
    print(f"Partido 1 ({partido1.equipo_local.nombre} vs {partido1.equipo_visitante.nombre}): {partido1.resultado.obtener_resultado()}")
    print(f"Partido 2 ({partido2.equipo_local.nombre} vs {partido2.equipo_visitante.nombre}): {partido2.resultado.obtener_resultado()}")
    
    # Asignar puntos
    def asignar_puntos(equipo, goles, goles_oponente):
        if goles > goles_oponente:
            equipo.puntos += 3  # Victoria
        elif goles < goles_oponente:
            equipo.puntos += 0  # Derrota
        else:
            equipo.puntos += 1  # Empate
    
    # Actualizar puntos
    asignar_puntos(equipo_A, 2, 2)  # Partido 1
    asignar_puntos(equipo_B, 2, 2)  # Partido 1
    asignar_puntos(equipo_B, 1, 0)  # Partido 2
    asignar_puntos(equipo_A, 0, 1)  # Partido 2
    
    # Mostrar tabla de posiciones
    estadisticas = EstadisticaCampeonato([equipo_A, equipo_B])
    tabla_posiciones = estadisticas.obtener_tabla_posiciones()
    
    print("\nTabla de Posiciones:")
    for posicion, equipo in tabla_posiciones:
        print(f"Posición {posicion}: {equipo.nombre} - {equipo.puntos} puntos")

if __name__ == "__main__":
    main()
