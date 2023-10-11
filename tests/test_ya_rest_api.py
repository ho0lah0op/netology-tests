import pytest
import time
from ya_rest_api import create_new_folder, check_folder_existence, delete_folder


YA_TOKEN = ""
YA_TOKEN2 = "blabla2"
headers = {
    'Authorization': 'OAuth {}'.format(YA_TOKEN)
}
headers2 = {
    'Authorization': 'OAuth {}'.format(YA_TOKEN2)
}


@pytest.fixture
def foldername():
    return "TestFolder_Louiz"


# Test 1: Позитивный - статус код равен 201 (папка создана)
def test_create_new_folder(foldername):
    status_code = create_new_folder(headers, foldername)
    assert status_code == 201


# Test 2: Негативный - статус код равен 409 (попытка создания папки с тем же именем)
def test_create_new_folder_negative(foldername):
    status_code = create_new_folder(headers, foldername)
    assert status_code == 409


# Test 3: Позитивный - статус код равен 200 (папка существует)
def test_check_folder_existence(foldername):
    status_code = check_folder_existence(headers, foldername)
    assert status_code == 200


# Test 4: Позитивный - запрос get выполняется меньше, чем за 1 сек (папка существует)
def test_check_folder_time(foldername):
    start_time = time.time()
    check_folder_existence(headers, foldername)
    end_time = time.time()
    execution_time = end_time - start_time
    assert execution_time <= 1.0


# Test 5: Негативный - статус код равен 401 (проверка папки с неправильным токеном)
def test_check_folder_existence_wrong_token(foldername):
    status_code = check_folder_existence(headers2, foldername)
    assert status_code == 401


# Test 6: Позитивный - статус код равен 204 (папка удалена)
def test_delete_folder(foldername):
    status_code = delete_folder(headers, foldername)
    assert status_code == 204


# Test 7: Негативный - статус код равен 404 (попытка удаления несуществующей папки)
def test_delete_folder_nonexisting(foldername):
    status_code = delete_folder(headers, foldername)
    assert status_code == 404


if __name__ == "__main__":
    pytest.main()