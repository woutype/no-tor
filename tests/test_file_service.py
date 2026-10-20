from file_service import get_info_file, format_file_size
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