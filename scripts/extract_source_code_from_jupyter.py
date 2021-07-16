from pathlib import Path
import json

folder = Path(__file__).parent.parent / 'others' / 'numpy_journey'
out_folder = Path(__file__).parent.parent.parent / 'Desktop' / 'python_folder'

def load_data(file):
    with file.open('r') as fr:
        data = json.load(fr)
        file_name = file.name.split('.')[0]
        write_data_to_file(data , file_name)

def write_data_to_file(data , file_name):
    file_extension = '.py'
    file_name += file_extension
    for cell in data['cells']:
        lines = cell['source']
        if len(lines) >= 1:
            with (out_folder / file_name).open('a') as fw:
                for line in lines:
                    fw.write(line + '\n')

def extract_data():
    for file in folder.iterdir():
        if file.is_file():
            load_data(file)

if __name__ == '__main__':
    extract_data()
