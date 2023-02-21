import requests


def berries():
    link = "https://pokeapi.co/api/v2/" + userin + "/" + userin2 + "/"
    print(link)
    api = requests.get(link)
    data = api.json()
    print(data.keys())


def contests():
    link = "https://pokeapi.co/api/v2/" + userin + "/" + userin2 + "/"
    print(link)
    api = requests.get(link)
    data = api.json()
    print(data.keys())
