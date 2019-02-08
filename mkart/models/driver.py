class Driver:

    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._laps = []

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def laps(self):
        return self._laps

    @laps.setter
    def laps(self, lap):
        self._laps.append(lap)
