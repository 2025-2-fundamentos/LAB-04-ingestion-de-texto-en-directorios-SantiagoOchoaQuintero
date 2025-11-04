def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    ... (docstring) ...
    """
    import os
    import pandas as pd
    import zipfile

    # --- INICIO DE LA MODIFICACIÓN ---
    # Ahora, 'output_dir' apunta a una carpeta DENTRO de 'files'
    output_dir = "files/output"
    # --- FIN DE LA MODIFICACIÓN ---

    input_dir = "input"
    zip_file_path = "files/input.zip"

    # 1. Crear el directorio de salida (files/output) si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 2. Descomprimir el archivo zip en el directorio raíz ('.')
    # Esto creará la carpeta 'input' en la raíz.
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall('.')

    # 3. El resto de tu código para procesar los archivos
    for dataset_type in ["train", "test"]:
        
        data = {"phrase": [], "target": []}
        
        for sentiment in ["negative", "positive", "neutral"]:
            dir_path = os.path.join(input_dir, dataset_type, sentiment)
            for filename in os.listdir(dir_path):
                if filename.endswith(".txt"):
                    file_path = os.path.join(dir_path, filename)
                    with open(file_path, "r", encoding="utf-8") as file:
                        phrase = file.read().strip()
                        data["phrase"].append(phrase)
                        data["target"].append(sentiment)

        df = pd.DataFrame(data)
        
        # 4. 'os.path.join' usará la nueva ruta para guardar el archivo
        # (ej: "files/output/train_dataset.csv")
        output_file = os.path.join(output_dir, f"{dataset_type}_dataset.csv")
        df.to_csv(output_file, index=False)