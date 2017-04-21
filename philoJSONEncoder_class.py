from flask.json import JSONEncoder

from philosopher import Philosopher


class PhiloJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Philosopher):
            return {'name': obj.name}

        return super(PhiloJSONEncoder, self).default(obj)
