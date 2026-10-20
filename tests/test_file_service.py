from file_service import (
    get_info_file,
    format_file_size,
    generate_token,
    prepare_share,
)
import pytest


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