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

    output_dir = "files/output"

    input_dir = "input"
    zip_file_path = "files/input.zip"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall('.')
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
    
        output_file = os.path.join(output_dir, f"{dataset_type}_dataset.csv")
        df.to_csv(output_file, index=False)