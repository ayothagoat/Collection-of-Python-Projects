import os

class FileSystem:
    def init(self, root_folder):
        self.root_folder = root_folder

    def create_folder(self, folder_name):
        path = self.root_folder + '/' + folder_name
        if not os.path.exists(path):
            os.mkdir(path)

    def delete_folder(self, folder_name):
        path = self.root_folder + '/' + folder_name
        if os.path.exists(path):
            os.rmdir(path)

    def create_file(self, folder_name, file_name):
        path = self.root_folder + '/' + folder_name + '/' + file_name
        open(path, 'a').close()

    def delete_file(self, folder_name, file_name):
        path = self.root_folder + '/' + folder_name + '/' + file_name
        if os.path.exists(path):
            os.remove(path)

file_system = FileSystem('documents')

file_system.create_folder('Financials')

file_system.create_file('Financials', 'budget.xlsx')

file_system.delete_file('Financials', 'budget.xlsx')

file_system.delete_folder('Financials')