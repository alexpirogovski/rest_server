from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from philosopher import Philosopher
from chopsticks import Chopsticks
from philoJSONEncoder_class import PhiloJSONEncoder
import logging

# from my_obj_class import MyObj


app = FlaskAPI(__name__)
philosophers_list = []
logging.basicConfig(format='[%(asctime)s]:%(name)s:%(levelname)s:%(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)

chopsticks = Chopsticks(5)

app.json_encoder = PhiloJSONEncoder


@app.route("/add", methods=['POST'])
def add():
    if request.method == 'POST':
        if len(philosophers_list) < 5:
            name = str(request.data.get('name', ''))
            new_philo = Philosopher(name, chopsticks)
            philosophers_list.append(new_philo)
            return {"Status": "Added."}, status.HTTP_201_CREATED
        else:
            return {"Error": "Too many philosophers."}, status.HTTP_409_CONFLICT
    # else:
    #     return {"Error": "Only POST method is supported."}, status.HTTP_400_BAD_REQUEST


def remove():
    pass

@app.route("/start", methods=['GET'])
def start():
    if request.method == 'GET':
        [phil.start() for phil in philosophers_list]
        [phil.join() for phil in philosophers_list]
        log.info("All done")
        return {"Status": "Completed!"}, status.HTTP_200_OK
    else:
        return {"Error": "Only GET method is supported."}, status.HTTP_400_BAD_REQUEST

@app.route("/remove", methods=['DELETE'])
def remove():
    if request.method == 'DELETE':
        name = str(request.data.get('name', ''))
        for phil in philosophers_list:
            if phil.name == name:
                philosophers_list.remove(phil)
                return {"Status": "Removed"}, status.HTTP_204_NO_CONTENT

        return {"Error": "Philosopher not found."}, status.HTTP_404_NOT_FOUND

@app.route("/list", methods = ['GET'])
def list():
    if request.method == 'GET':
        return jsonify(philosophers_list)

if __name__ == "__main__":
    app.run("0.0.0.0", 8081, debug=True)
