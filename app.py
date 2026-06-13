from flask import Flask, jsonify, request

app = Flask(__name__)

taches = []

@app.route('/taches', methods=['GET'])
def get_tache():
    return jsonify(taches)



@app.route('/taches', methods=['POST'])
def post_taches():
    data = request.get_json()
    taches.append(data["titre"])
    return jsonify({"message":"Tâche ajoutée !"})



@app.route('/')
def accueil():
    return "Hello, ça marche !"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
