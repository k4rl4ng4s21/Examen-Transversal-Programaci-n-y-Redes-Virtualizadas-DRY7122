import geopy.distance
import time

def obtener_coordenadas(ciudad):
    coordenadas = {
        'Santiago': (-33.4489, -70.6693),
        'Lima': (-12.0464, -77.0428),
        # Puedes agregar más ciudades y sus coordenadas aquí
    }
    return coordenadas.get(ciudad, None)

def calcular_distancia(origen, destino):
    coords_origen = obtener_coordenadas(origen)
    coords_destino = obtener_coordenadas(destino)
    
    if not coords_origen or not coords_destino:
        return None
    
    distancia_km = geopy.distance.geodesic(coords_origen, coords_destino).km
    distancia_millas = geopy.distance.geodesic(coords_origen, coords_destino).miles
    return distancia_km, distancia_millas

def calcular_duracion(distancia_km, medio_transporte):
    velocidades = {
        'auto': 80, # km/h
        'bus': 60,  # km/h
        'avión': 800, # km/h
    }
    velocidad = velocidades.get(medio_transporte, None)
    if not velocidad:
        return None
    duracion_horas = distancia_km / velocidad
    return duracion_horas

def narrativa_viaje(origen, destino, distancia_km, distancia_millas, duracion_horas, medio_transporte):
    narrativa = f"Viaje desde {origen} hasta {destino}:\n"
    narrativa += f"Distancia: {distancia_km:.2f} km ({distancia_millas:.2f} millas).\n"
    narrativa += f"Duración estimada del viaje en {medio_transporte}: {duracion_horas:.2f} horas.\n"
    return narrativa

def main():
    while True:
        print("Ingrese la ciudad de origen (o 'e' para salir): ")
        origen = input().strip()
        if origen.lower() == 'e':
            break
        
        print("Ingrese la ciudad de destino: ")
        destino = input().strip()
        
        print("Elija el medio de transporte (auto, bus, avión): ")
        medio_transporte = input().strip().lower()
        
        distancia = calcular_distancia(origen, destino)
        if not distancia:
            print("Una o ambas ciudades no son válidas. Intente de nuevo.")
            continue
        
        distancia_km, distancia_millas = distancia
        duracion_horas = calcular_duracion(distancia_km, medio_transporte)
        
        if duracion_horas is None:
            print("Medio de transporte no válido. Intente de nuevo.")
            continue
        
        narrativa = narrativa_viaje(origen, destino, distancia_km, distancia_millas, duracion_horas, medio_transporte)
        print(narrativa)

if __name__ == "__main__":
    main()




