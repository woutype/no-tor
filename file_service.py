import os


def get_info_file(file_path: str) -> dict:

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    return {
        "name": file_name,
        "size": file_size,
    }