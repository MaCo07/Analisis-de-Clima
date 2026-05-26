import os
import pandas as pd
import matplotlib.pyplot as plt
# Iniciamos las variables en cero para ir sumando los datos linea por linea
def analizar_clima(ruta_datos, ruta_resultados):
    suma_maximas = 0.0
    suma_minimas = 0.0
    total_precipitacion = 0.0
    dias_validos = 0
    
    # Listas para guardar solo los datos de enero para el grafico
    anios_enero = []
    temperaturas_enero = []

    # Usamos with para abrir el archivo asi se cierra solo cuando termina y no gasta memoria
    try:
        with open(ruta_datos, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

            # Si el archivo tiene 1 linea o menos, es porque solo tiene los titulos o esta vacio
            if len(lineas) <= 1:
                return
            # Hacemos un for empezando desde el 1 para saltarnos los titulos de las columnas (la linea 0)
            for i in range(1, len(lineas)):
                linea = lineas[i].strip() # strip saca los espacios en blanco al principio y al final
                if not linea: # Si la linea esta vacia por algun error, pasamos a la siguiente
                    continue 
                columnas = linea.split(';') if ';' in linea else linea.split(',')
                # Nos fijamos que tenga las 6 columnas completas (Año, Mes, Max, Min, Media, Lluvia)
                if len(columnas) >= 6:
                    anio = columnas[0].strip()
                    mes = columnas[1].strip()
                    try:
                        # Le cambiamos la coma por punto a los decimales porque sino Python no lo toma como numero
                        # y despues lo pasamos a float para poder hacer calculos matematicos
                        maxima = float(columnas[2].strip().replace(',', '.'))
                        minima = float(columnas[3].strip().replace(',', '.'))
                        media = float(columnas[4].strip().replace(',', '.'))
                        precipitacion = float(columnas[5].strip().replace(',', '.'))
                        # Acumulamos los valores sumandolos para sacar los promedios al final
                        suma_maximas += maxima
                        suma_minimas += minima
                        total_precipitacion += precipitacion
                        dias_validos += 1
                        # Aca filtramos solo enero y guardamos la temperatura media y el año en las listas
                        # Lo pasamos a minuscula con .lower() por si en el csv dice 'Enero' o 'enero
                        if mes.lower() == 'enero':
                            anios_enero.append(anio)
                            temperaturas_enero.append(media)
                    except ValueError:
                        continue
    except Exception:
        return
# Validacion para no dividir por cero si el archivo estaba todo roto
    if dias_validos == 0:
        return
# Calculamos los promedios dividiendo la suma total por la cantidad de dias que contamos
    promedio_max = suma_maximas / dias_validos
    promedio_min = suma_minimas / dias_validos
# Generacion de informe en archivo txt
    try:
        # Si no existe la carpeta para guardar los resultados, le decimos al sistema que la cree
        if not os.path.exists(ruta_resultados):
            os.makedirs(ruta_resultados)
        ruta_informe = os.path.join(ruta_resultados, 'informe_climatico.txt')
        # Escribimos los resultados calculados en un txt nuevo
        with open(ruta_informe, 'w', encoding='utf-8') as f:
            f.write("=== REPORTE CLIMÁTICO GENERAL ===\n")
            f.write(f"Registros válidos analizados: {dias_validos}\n")
            f.write(f"Temperatura Máxima Promedio: {promedio_max:.2f}°C\n")
            f.write(f"Temperatura Mínima Promedio: {promedio_min:.2f}°C\n")
            f.write(f"Precipitación Total Acumulada: {total_precipitacion:.2f} mm\n")
    except Exception:
        pass
# Generacion de grafico basico usando pandas libreria
    try:
        if len(anios_enero) > 0:
            # Armamos un dataframe (que es basicamente una tabla) usando las dos listas de enero
            df_grafico = pd.DataFrame({'Año': anios_enero, 'Temp_Media_Enero': temperaturas_enero})
            # Ordenamos por año para que la linea del grafico vaya de izquierda a derecha y no se cruce
            df_grafico = df_grafico.sort_values(by='Año')
            # Dibujamos el grafico de linea y le ponemos color y marcadores redondos a los puntos
            plt.figure(figsize=(10, 5))
            df_grafico.plot(x='Año', y='Temp_Media_Enero', kind='line', ax=plt.gca(), color='blue', marker='o')
            # Titulos de los bordes del grafico
            plt.title('Evolución Histórica de la Temperatura Media en Enero')
            plt.xlabel('Año')
            plt.ylabel('Temperatura Media (°C)')
            plt.grid(True, linestyle='--', alpha=0.6)
            plt.tight_layout() 
            plt.savefig(os.path.join(ruta_resultados, 'grafico_evolucion_enero.png'))
    except Exception:
        pass

if __name__ == "__main__":
    analizar_clima("./datos/clima.csv", "./resultados")
