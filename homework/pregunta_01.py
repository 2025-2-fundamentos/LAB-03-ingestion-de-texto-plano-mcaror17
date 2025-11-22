"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
import pandas as pd
import re

def pregunta_01():
    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Saltar encabezado y línea de guiones
    content_lines = [line.rstrip("\n") for line in lines[3:] if line.strip()]

    clusters = []
    cluster_num = None
    cantidad = None
    porcentaje = None
    palabras = []

    for line in content_lines:
        match = re.match(r"^\s*(\d+)\s+(\d+)\s+([\d,]+)\s*%\s*(.*)", line)
        if match:
            # Guardar cluster anterior
            if cluster_num is not None:
                # Unir líneas de palabras clave
                palabras_str = " ".join(palabras)
                # Normalizar espacios y comas
                palabras_str = re.sub(r"\s*,\s*", ", ", palabras_str)  # coma + un espacio
                palabras_str = re.sub(r"\s+", " ", palabras_str).strip()  # un solo espacio
                palabras_str = palabras_str.rstrip(".")  # quitar punto final

                clusters.append({
                    "cluster": int(cluster_num),
                    "cantidad_de_palabras_clave": int(cantidad),
                    "porcentaje_de_palabras_clave": float(porcentaje.replace(",", ".")),
                    "principales_palabras_clave": palabras_str
                })

            # Nuevo cluster
            cluster_num, cantidad, porcentaje, palabra = match.groups()
            palabras = [palabra.strip()]
        else:
            # Continuación de palabras clave
            palabras.append(line.strip())

    # Guardar último cluster
    palabras_str = " ".join(palabras)
    palabras_str = re.sub(r"\s*,\s*", ", ", palabras_str)
    palabras_str = re.sub(r"\s+", " ", palabras_str).strip()
    palabras_str = palabras_str.rstrip(".")

    clusters.append({
        "cluster": int(cluster_num),
        "cantidad_de_palabras_clave": int(cantidad),
        "porcentaje_de_palabras_clave": float(porcentaje.replace(",", ".")),
        "principales_palabras_clave": palabras_str
    })

    df = pd.DataFrame(clusters)
    return df