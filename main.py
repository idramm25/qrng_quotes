import requests
import json
from eng import var as v
# from rus import var as v

URL = 'https://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint8'


def func():
    response = requests.get(URL)
    json_str = json.dumps(response.json())
    data = json.loads(json_str)
    x = int(data['data'][0])
    d = round((x / 255) * 100)
    print(v[d])


if __name__ == '__main__':
    func()
