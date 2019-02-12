class Driver:

    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._average_speed = ''

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def average_speed(self):
        return self._average_speed

    @average_speed.setter
    def average_speed(self, value):
        self._average_speed = value
