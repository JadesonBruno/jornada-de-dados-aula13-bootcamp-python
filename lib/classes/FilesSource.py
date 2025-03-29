# Import libs nativas
import os

# Import módulos
from .AbstractDataSource import AbstractDataSource


class FilesSources(AbstractDataSource):
    def __init__(self):
        self.previus_files = []
        self.start()

    def start(self):
        self.create_path()

    def create_path(self):
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, "data", "extension_files")
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previus_files]

        if new_files:
            print("New files detected:", new_files)
            # Atualizando lista com arquivos anteriores
            self.previus_files = current_files
        else:
            print("Novos arquivos não dectados.")

    def get_data(self):
        pass

    def transform_data_to_df(self):
        pass

    def save_data(self):
        pass

    def show_files(self):
        pass
