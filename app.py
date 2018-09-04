from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/pokemon/<poke_id>', methods=['GET'])
def get_pokemon_by_id(poke_id):
    r = requests.get('http://pokeapi.co/api/v2/pokemon/{}'.format(poke_id))
    poke_name = r.json()['name']
    return render_template("index.html",poke_id=poke_id, poke_name=poke_name)

if __name__ == '__main__':
    app.run()
