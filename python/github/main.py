import requests
import json
import markdown
from http import HTTPStatus


def main():
    url = "https://api.github.com/repos/chipk215/exercism/contents/python"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == HTTPStatus.OK:
        results = json.loads(response.text)
        for item in results:
            print(f"Name: {item['name']}.  Type: {item['type']}")

        item_url = url + '/' + results[1]['name']
        item_response = requests.request("GET", item_url, headers=headers, data=payload)
        if item_response.status_code == HTTPStatus.OK:
            item_results = json.loads(item_response.text)
            file_items = [item for item in item_results if item['type'] == 'file']
            print(file_items)
            readme_url = file_items[0]['download_url']
            print(f"readme url = {readme_url}")
            readme_response = requests.get(readme_url)
            readme_html = markdown.markdown(readme_response.text)
            print("****")
            print(readme_html)


if __name__ == "__main__":
    main()
