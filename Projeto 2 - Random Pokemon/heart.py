import requests;
import json;

def pokemon(nome):

    url = 'https://pokeapi.co/api/v2/pokemon/'
    url = url + nome

    r = requests.get(url, auth=('user', 'pass'))
    pk_data = r.json()
    json_string = json.dumps(pk_data) 
    data_dict = json.loads(json_string)
    new_data_dict = data_dict.get('forms')
    pk_name = new_data_dict[0]['name']
  
    return pk_name