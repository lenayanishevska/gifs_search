import requests


def search_gif_by_string(search_string):
    url = 'https://api.giphy.com/v1/gifs/search?'

    params = {
        "api_key": '4ocgt4ftUYnfJ9AJPEwNmQY9PlqWxWtw',
        "q": search_string,
        "limit": 3,
    }

    try:
        response = requests.get(url, params)
        data = response.json()

        if response.status_code == 200:
            gif_links = [item["images"]["original"]["url"] for item in data["data"]]
            return gif_links
        else:
            print(f"Error: {data['meta']['msg']}")

    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")