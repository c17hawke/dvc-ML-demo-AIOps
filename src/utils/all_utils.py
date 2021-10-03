import yaml
import os

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content


def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"directory is created at {dir_path}")


def save_local_df(data, data_path, index_status=False):
    data.to_csv(data_path, index=index_status)
    print(f"data is saved at {data_path}")