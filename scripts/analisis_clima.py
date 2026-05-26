import os
import pandas as pd
import matplotlib.pyplot as plt

def analizar_clima(ruta_datos, ruta_resultados):
    suma_maximas = 0.0
    suma_minimas = 0.0
    total_precipitacion = 0.0
    dias_validos = 0
    anios_enero = []
    temperaturas_enero = []

    try:
        with open(ruta_datos, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            if len(lineas) <= 1:
                return
            for i in range(1, len(lineas)):
                linea = lineas[i].strip()
                if not linea:
                    continue 
                columnas = linea.split(';') if ';' in linea else linea.split(',')
                if len(columnas) >= 6:
                    anio = columnas[0].strip()
                    mes = columnas[1].strip()
                    try:
                        maxima = float(columnas[2].strip().replace(',', '.'))
                        minima = float(columnas[3].strip().replace(',', '.'))
                        media = float(columnas[4].strip().replace(',', '.'))
                        precipitacion = float(columnas[5].strip().replace(',', '.'))
                        suma_maximas += maxima
                        suma_minimas += minima
                        total_precipitacion += precipitacion
                        dias_validos += 1
                        if mes.lower() == 'enero':
                            anios_enero.append(anio)
                            temperaturas_enero.append(media)
                    except ValueError:
                        continue
    except Exception:
        return

    if dias_validos == 0:
        return

    promedio_max = suma_maximas / dias_validos
    promedio_min = suma_minimas / dias_validos

    try:
        if not os.path.exists(ruta_resultados):
            os.makedirs(ruta_resultados)
        ruta_informe = os.path.join(ruta_resultados, 'informe_climatico.txt')
        with open(ruta_informe, 'w', encoding='utf-8') as f:
            f.write("=== REPORTE CLIMÁTICO GENERAL ===\n")
            f.write(f"Registros válidos analizados: {dias_validos}\n")
            f.write(f"Temperatura Máxima Promedio: {promedio_max:.2f}°C\n")
            f.write(f"Temperatura Mínima Promedio: {promedio_min:.2f}°C\n")
            f.write(f"Precipitación Total Acumulada: {total_precipitacion:.2f} mm\n")
    except Exception:
        pass

    try:
        if len(anios_enero) > 0:
            df_grafico = pd.DataFrame({'Año': anios_enero, 'Temp_Media_Enero': temperaturas_enero})
            df_grafico = df_grafico.sort_values(by='Año')
            plt.figure(figsize=(10, 5))
            df_grafico.plot(x='Año', y='Temp_Media_Enero', kind='line', ax=plt.gca(), color='blue', marker='o')
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
