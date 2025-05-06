from wav_utils import ProcesadorWav
from config import *

# Este script procesa un archivo de audio WAV estéreo extrayendo el canal derecho, 
# invirtiendo su contenido temporal,
# reduciendo su frecuencia de muestreo y guardando el resultado como un nuevo archivo mono. 
# Los parámetros de entrada
# y salida (archivos y frecuencias) están definidos en el archivo de config.py


def main():
    procesador = ProcesadorWav(
        archivo_entrada=ARCHIVO_ENTRADA,
        archivo_salida=ARCHIVO_SALIDA,
        freq_original=FRECUENCIA_ORIGINAL,
        freq_objetivo=FRECUENCIA_OBJETIVO
    )

    procesador.leer_archivo()
    procesador.extraer_canal_derecho()
    procesador.invertir_muestras()
    procesador.reducir_muestreo()
    procesador.guardar_archivo()

if __name__ == "__main__":
    main()