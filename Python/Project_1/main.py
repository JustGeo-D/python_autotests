import requests

URL = 'https://api.pokemonbattle.me/v2'
Token = '70f3daca6bc1cdef7b4eb82a727ea099'
Header = {'Content-type' : 'application/json', 'trainer_token':Token}
body_create = {
    "name": "LOLIK",
    "photo": "https://dolnikov.ru/pokemons/albums/009.png"
}


respons_create = requests.post(url= f'{URL}/pokemons', headers= Header, json= body_create)
print(respons_create.text)

pokemon_id = respons_create.json()['id']

body_izm = {
    "pokemon_id": pokemon_id,
    "name": "Roflik",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

respons_izm = requests.put(url= f'{URL}/pokemons', headers= Header, json= body_izm)
print(respons_izm.text)

body_add_pokeb = {
    "pokemon_id": pokemon_id
}

respons_add = requests.post(url= f'{URL}/trainers/add_pokeball', headers= Header, json= body_add_pokeb)
print(respons_add.text)