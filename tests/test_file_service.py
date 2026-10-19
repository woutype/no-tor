from file_service import get_info_file


def test_get_info_file_success(tmp_path):

    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello World")

    result = get_info_file(str(test_file))

    assert result["name"] == "test.txt"
    assert result["size"] == 11
