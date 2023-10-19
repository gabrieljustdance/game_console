from segundo import eleccion, carta_principal_nombre, carta_principal, estadisticas
from tercero import carta_segundaria, carta_segundaria_nombre, estadisticas_de_enemigo

ele = eleccion

print(f'tu personaje se llama {ele} buena suerte, en las batallas')

print('vas a tener una carta principal y esta va hacer = ' f"'{carta_principal_nombre}'" f" y vas a luchar contra = '{carta_segundaria_nombre}'")

print(f'tus estadisticas son {estadisticas}')
print(f'las estadisticas de la carta enemiga son {estadisticas_de_enemigo}')
 
#if carta_principal == carta_segundaria:
 #   print('las cartas estan iguales ')