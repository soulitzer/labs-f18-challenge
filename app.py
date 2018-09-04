from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/pokemon/<poke_str>', methods=['GET'])
def get_pokemon_by_id(poke_str):
    try:
        poke_id = int(poke_str)
        r = requests.get('http://pokeapi.co/api/v2/pokemon/{}'.format(poke_id))
        poke_name = r.json()['name']
        return render_template("index.html",poke_id=poke_id, poke_name=poke_name)
    except ValueError:
        r = requests.get('http://pokeapi.co/api/v2/pokemon/{}'.format(poke_str))
        poke_id = r.json()['id']
        return render_template("index2.html",poke_id=poke_id, poke_name=poke_str)


if __name__ == '__main__':
    app.run()
