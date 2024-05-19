import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
Token = '70f3daca6bc1cdef7b4eb82a727ea099'
Header = {'Content-type' : 'application/json', 'trainer_token':Token}
Trainer_ID = '2548'

def test_status_code():
    response = requests.get(url= f'{URL}/trainers', params= {'trainer_id' : Trainer_ID })
    assert response.status_code == 200

def test_name_requests():
    response_get = requests.get(url= f'{URL}/trainers', params= {'trainer_id' : Trainer_ID })
    assert response_get.json()["data"][0]["trainer_name"] == 'Lolnight'
    
