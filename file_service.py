import os
import uuid


def get_info_file(file_path: str) -> dict:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    return {
        "name": file_name,
        "size": file_size,
    }


def format_file_size(size_bytes: int) -> str:
    size_bytes = float(size_bytes)

    units = ["B", "KB", "MB", "GB", "TB"]

    for unit in units:
        if size_bytes >= 1024:
            size_bytes /= 1024
        else:
            if unit == 'B':
                return f"{int(size_bytes)} {unit}"
            return f"{size_bytes:.1f} {unit}"

    return f"{size_bytes:.1f} {units[-1]}"


def generate_token() -> str:
    return uuid.uuid4().hex


def prepare_share(file_path: str) -> dict:
    info = get_info_file(file_path)
    size_formatted = format_file_size(info["size"])

    return {
        "file_path": os.path.abspath(file_path),
        "file_name": info["name"],
        "file_size": size_formatted,
        "file_bytes_formatted": size_formatted,
        "file_bytes": info["size"],
        "file_icon": get_file_icon(info["name"]),
        "token": generate_token(),
    }


def get_file_icon(file_name: str) -> str:
    extension = file_name.lower().split(".")[-1] if '.' in file_name else ''

    icons = {
        'zip': 'zip',
        'rar': 'zip',
        '7z': 'zip',
        'tar': 'zip',
        'gz': 'zip',
        'png': 'png',
        'jpg': 'jpg',
        'jpeg': 'jpg',
        'pdf': 'pdf',
        'docx': 'docx',
        'doc': 'docx',
        'txt': 'txt',
        'md': 'txt',
        'log': 'txt',
    }

    return icons.get(extension, 'file')
