from flask import Flask, jsonify, Response,request
import mutantexmen
app = Flask (__name__)

@app.route('/')
def Index():

    return 'Proyecto MUTANTE X - ADN'

@app.route('/mutant',methods = ['POST'])
def run_api():
    content = request.get_json(force=True, silent = True)
    if not (request.get_json() is None) :
        if content and  "dna" in content:
            validateAdn = mutantexmen.Mutant()
            mutantes= validateAdn.isMutant(content)
            print(mutantes)
            return jsonify(adn=mutantes)

if __name__ == "__main__":
   app.run(port=5000, debug=True)