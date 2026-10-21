from file_service import (
    get_info_file,
    format_file_size,
    generate_token,
    prepare_share,
    get_file_icon,
    zip_folder,
)
import pytest
import os


def test_get_info_file_success(tmp_path):

    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello World")

    result = get_info_file(str(test_file))

    assert result["name"] == "test.txt"
    assert result["size"] == 11


def test_get_info_file_not_found():
    with pytest.raises(FileNotFoundError):
        get_info_file("file.txt")


def test_format_file_size():
    assert format_file_size(0) == "0 B"
    assert format_file_size(500) == "500 B"
    assert format_file_size(1024) == "1.0 KB"
    assert format_file_size(1024 * 1024) == "1.0 MB"
    assert format_file_size(1024 * 1024 * 1024) == "1.0 GB"


def test_generate_token():
    token1 = generate_token()
    token2 = generate_token()

    assert token1 != token2
    assert len(token1) == 32


def test_prepare_share(tmp_path):
    test_file = tmp_path / "archive.zip"
    test_file.write_text("12345")

    share = prepare_share(str(test_file))

    assert share["file_name"] == "archive.zip"
    assert share["file_size"] == "5 B"
    assert len(share["token"]) == 32
    assert share["file_path"] == str(test_file.resolve())
    assert share["file_icon"] == "zip"




def test_get_file_icon():
    assert get_file_icon("document.pdf") == "pdf"
    assert get_file_icon("archive.tar.gz") == "zip"
    assert get_file_icon("PHOTO.PNG") == "png"
    assert get_file_icon("script.py") == "file"
    assert get_file_icon("no_extension") == "file"


def test_zip_folder(tmp_path):
    test_dir = tmp_path / "files"
    test_dir.mkdir()
    (test_dir / "secrets.png").write_text("my-secret-key")

    zip_path = zip_folder(str(test_dir))

    assert os.path.isfile(zip_path)
    assert zip_path.endswith(".zip")

    os.remove(zip_path)


def test_zip_folder_not_a_dir(tmp_path):
    fake_file = tmp_path / "file.txt"
    fake_file.write_text("hello")

    with pytest.raises(NotADirectoryError):
        zip_folder(str(fake_file))


def test_prepare_share_folder(tmp_path):
    test_dir = tmp_path / "folder"
    test_dir.mkdir()
    (test_dir / "code.py").write_text("print('TOKEN')")

    share = prepare_share(str(test_dir))

    assert share["file_name"] == "folder.zip"
    assert share["file_icon"] == "zip"
    assert share["is_temp"] is True
    assert os.path.isfile(share["file_path"])

    os.remove(share["file_path"])