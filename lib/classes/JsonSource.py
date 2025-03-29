# Import libs nativas
import os

# Import libs terceiros
import pandas as pd

# Import módulos
from .FilesSource import FilesSources


class JsonSource(FilesSources):
    def create_path(self):
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, "data", "json_files")
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previus_files and file.endswith(".json")]

        if new_files:
            print("Novos arquivos json detectados: ", new_files)
            # Atualizando lista com arquivos anteriores
            self.previus_files = current_files
        else:
            print("Nenhum arquivo json detectado.")
            self.get_data()

    def get_data(self):
        """
        Implementa o carregar dados do json na pasta específica.
        """
        dataframes = []
        for filepath in self.previus_files:
            try:
                path = f"{self.folder_path}/{filepath}"
                data = pd.read_json(path)
                dataframes.append(data)
            except Exception as e:
                print("Ocorreu um erro durante leitura do json: ", e)

        if dataframes:
            self.combinated_data = pd.concat(dataframes, ignore_index=True)
            print(self.combinated_data)

    def transform_data_to_df(self):
        return super().transform_data_to_df()
