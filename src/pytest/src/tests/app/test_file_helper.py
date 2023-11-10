import pytest
import os

from unittest import mock
from dev.app.file_helper import Api, FileHelper

@pytest.fixture
def temp_file(tmp_path):
    f = tmp_path / "filename"
    # print(f"\n{f}\n")
    # /tmp/pytest-of-avorotyn/pytest-9/test_remove_file0/filename
    f.write_text("CONTENT")
    return f

@pytest.fixture
def api():
    api = Api("api_key_secret")
    print("api fixture called")
    yield api
    api.close()

@pytest.fixture
def fh(api):
    fh = FileHelper(api)
    return fh

class TestFileHelper:

    def test_init(self):
        print("\ntest_init")
        api = object()
        fh = FileHelper(api)
        assert fh.api is api

    def test_remove_file(self, temp_file):
        print("\ntest_remove_file")
        api = object()
        fh = FileHelper(api)
        fh.remove_file(temp_file)
        assert os.path.exists(temp_file) is False

    @mock.patch.object(FileHelper, "prepare_file")
    def test_upload_file(self, mocked_prepare_file):
        print("\ntest_upload_file")
        fake_api = mock.MagicMock()
        # expected_data = object()
        # mocked_prepare_file.return_value = expected_data
        print(f"\n{fake_api}")
        fh = FileHelper(fake_api)
        fh.upload_file("fake filepath")
        # fake_api.request.assert_called()
        # fake_api.request.assert_called_once()
        # fake_api.request.assert_called_once_with("POST", expected_data)
        fake_api.request.assert_called_once_with(
            "POST", mocked_prepare_file.return_value)



# https://docs.pytest.org/en/6.2.x/tmpdir.html

