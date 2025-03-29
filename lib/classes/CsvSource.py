# Import libs nativas
import os

# Import libs terceiros
import pandas as pd

# Import módulos
from .FilesSource import FilesSources


class CsvSource(FilesSources):
    def create_path(self):
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, "data", "csv_files")
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previus_files and file.endswith(".csv")]

        if new_files:
            print("Novo arquivo detectado: ", new_files)
            # Atualizando lista com arquivos anteriores
            self.previus_files = current_files
        else:
            print("Nenhum arquivo csv detectado.")
            self.get_data()

    def get_data(self):
        """
        Implementa o carregar dados do csv na pasta específica.
        """
        dataframes = []
        for file_path in self.previus_files:
            try:
                path = f"{self.folder_path}/{file_path}"
                data = pd.read_csv(path)
                dataframes.append(data)
            except Exception as e:
                print(f"Ocorreu um erro durante leitura do csv: {e}")

        if dataframes:
            self.combined_data = pd.concat(dataframes, ignore_index=True)
            print(self.combined_data)
        else:
            return None

    def transform_data_to_df(self):
        return super().transform_data_to_df()
