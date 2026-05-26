# Analisis-de-Clima
Proyecto de la Materia Organización Empresarial, desarrollo de un trabajo practico sobre análisis de datos CSV sobre datos reales

# Titulo Proyecto : Informe clima en Ciudad de Buenos Aires periodo 1991 - 2020
Se adquirio el siguiente archivo CSV en la pagina oficial del gobierno de la Ciudad de Buenos Aires, ademas se añadio la columna de precipataciones con valores simulados por mes, para cumplir con los requisitos minimos del TP. Estos valores fueron generados y simulados con la IA de Gemini.

# Integrantes 
- Matias Miguel Colque Fabian (Persona Real)
- Hugo Lider (ficticio)
- Desarrollador Paco (ficticio)
- QA Luis (ficticio)

# Escenario elegido
Se eligio el escenario de datos climaticos registrados en la Ciudad de Buenos Aires.

# Descripcion de Dataset
El dataset cuenta originalmente con los datos de fecha, temperaturas maximas y minimas ademas del promedio por mes. Ademas como se dijo anteriormente se genero de forma simulada a traves de Gemini, la columna de precipitacion. Esta generacion se baso tambien en los meses del año y los mas propensos a lluvias, como veremos en los meses de verano son los registros con mas precipitaciones.

# Instrucciones Básicas para Ejecutar el Script

**Paso 1: Clonar el repositorio**
Abre tu terminal y clona este proyecto en tu máquina local:

git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DE_LA_CARPETA>

**Paso 2: Verificar los datos**
Asegúrate de que el archivo de datos original (clima.csv) se encuentre dentro de la carpeta datos/.

**Paso 3: Ejecutar el análisis**
python scripts/analisis_clima.py

**Paso 4: Revisar los resultados**
Se genera un archivo tipo txt y un grafico simple

# Codigo revisado por QA
Se verifico la estructura de carpetas, codigo, comentarios, funcionamiento del mismo, resultados esperados.
