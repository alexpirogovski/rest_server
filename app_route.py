from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from philosopher import Philosopher
from philoJSONEncoder_class import PhiloJSONEncoder
# from my_obj_class import MyObj


app = FlaskAPI(__name__)
items = []

app.json_encoder = PhiloJSONEncoder
@app.route("/", methods=['GET', 'POST'])
def philos():
    if request.method == 'POST':
        suka = Philosopher("Puper")
        items.append(suka)
        name = str(request.data.get('name', ''))
        # age = request.data.get('name', '')
        # return name
        pidr = Philosopher(name)
        items.append(pidr)
        return jsonify(items)
        # for i in items:
        #     return i.to_json()




if __name__ == "__main__":
    app.run("0.0.0.0", 8081, debug=True)