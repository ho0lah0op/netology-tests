import requests
from urllib.parse import quote

YA_TOKEN = ""
headers = {
    'Authorization': 'OAuth {}'.format(YA_TOKEN)
}


def create_new_folder(headers, foldername):
    url = f"https://cloud-api.yandex.net/v1/disk/resources?path={quote(foldername)}"
    response = requests.put(url=url, headers=headers)
    print(response.status_code)
    return response.status_code


def check_folder_existence(headers, foldername):
    url = f"https://cloud-api.yandex.net/v1/disk/resources?path={quote(foldername)}"
    response = requests.get(url=url, headers=headers)
    print(response.status_code)
    return response.status_code


def delete_folder(headers, foldername):
    url = f'https://cloud-api.yandex.net/v1/disk/resources?path={quote(foldername)}'
    response = requests.delete(url=url, headers=headers)
    print(response.status_code)
    return response.status_code


if __name__ == '__main__':
    create_new_folder(headers, 'TestFolder_Louiz')
    check_folder_existence(headers, "TestFolder_Louiz")
    delete_folder(headers, "TestFolder_Louiz")