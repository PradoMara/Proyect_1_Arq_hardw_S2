import wave 
import struct 

def leer_archivo_wav(archivo):
    with wave.open(archivo, "rb") as archivo_wave:
        parametros = archivo_wave.getparams() # obtiene n_canales, ancho_muestra, frecuencia_muestreo, n_frames, tipo_comp, nombre_comp
        frames = archivo_wave.readframes(parametros.nframes)
    return frames, parametros

def extraer_canal_derecho(frames, parametros): 
    n_canales = parametros.nchannels
    ancho_muestra = parametros.sampwidth
    n_frames = parametros.nframes

    canal_derecho = []	

    for i in range(n_frames):
        offset = i * n_canales * ancho_muestra
        muestra_derecha_bytes = frames[offset + ancho_muestra: offset + 2 * ancho_muestra]
        muestra_derecha = struct.unpack("<h", muestra_derecha_bytes)[0]
        canal_derecho.append(muestra_derecha)

    return canal_derecho

def invertir_audio(muestras):
    return list(reversed(muestras))

def reducir_muestreo(muestras, factor_reduccion):
    return muestras[::factor_reduccion]

def guardar_archivo_wav(archivo, muestras, frecuencia_muestreo):
    with wave.open(archivo, "wb") as wav:
        wav.setnchannels(1)  # Mono
        wav.setsampwidth(2) 
        wav.setframerate(frecuencia_muestreo)

        frames_codificados = b''.join(struct.pack('<h', muestra) for muestra in muestras)
        wav.writeframes(frames_codificados)

