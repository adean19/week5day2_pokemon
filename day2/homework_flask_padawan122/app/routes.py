from flask import render_template, request
from app import app
from .forms import PokemonForm
import requests, json

@app.route('/', methods=["GET","POST"])
def home_page():
    form = PokemonForm()
    pokemon_data = {}
    if request.method == "GET":
        pass
    else:
        pokemon_apicall = f'https://pokeapi.co/api/v2/pokemon/{form.pokemon_name.data.lower()}'
        pokemon_apicall_response = requests.get(pokemon_apicall)
        if pokemon_apicall_response.ok == True:
            pokemon_data = {'Name': pokemon_apicall_response.json()['forms'][0]['name'],
                            'Ability': pokemon_apicall_response.json()['abilities'][0]['ability']['name'],
                            'Stats': {'HP': pokemon_apicall_response.json()['stats'][0]['base_stat'],
                                      'Defense': pokemon_apicall_response.json()['stats'][2]['base_stat'],
                                      'Attack' : pokemon_apicall_response.json()['stats'][1]['base_stat']},
                            'Sprite': pokemon_apicall_response.json()['sprites']['front_shiny']}
    return render_template('index.html', title='Home', form=form, pokemon_data=pokemon_data)