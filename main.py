from wav_utils import *
from config import *

# Este script procesa un archivo de audio WAV estéreo extrayendo el canal derecho, invirtiendo su contenido temporal,
# reduciendo su frecuencia de muestreo y guardando el resultado como un nuevo archivo mono. Los parámetros de entrada
# y salida (archivos y frecuencias) están definidos en el archivo de configuración.

def main():
    frames, parametros = leer_archivo_wav(ARCHIVO_ENTRADA)
    print(f"[INFO] Archivo WAV original: {parametros}")

    canal_derecho = extraer_canal_derecho(frames, parametros)
    invertido = invertir_audio(canal_derecho)
    reducido = reducir_muestreo(invertido, FRECUENCIA_ORIGINAL // FRECUENCIA_OBJETIVO)

    guardar_archivo_wav(ARCHIVO_SALIDA, reducido, FRECUENCIA_OBJETIVO)
    print(f"[INFO] Archivo procesado guardado como: {ARCHIVO_SALIDA}")

if __name__ == "__main__":
    main()