import requests;
import json;



def pokemon(nome):

    url = 'https://pokeapi.co/api/v2/pokemon/'
    url = url + nome

    print (url)
    r = requests.get(url, auth=('user', 'pass'))
    x = r.json();

    print(json.dumps(x, indent=4));
    return x