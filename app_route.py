from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from philosopher import Philosopher
# from my_obj_class import MyObj


app = FlaskAPI(__name__)
items = []


@app.route("/", methods=['GET', 'POST'])
def philos():
    if request.method == 'POST':
        name = str(request.data.get('name', ''))
        # age = request.data.get('name', '')
        pidr = Philosopher(name)
        items.append(pidr)
        return jsonify(item = items[i])



if __name__ == "__main__":
    app.run("0.0.0.0", 8081, debug=True)