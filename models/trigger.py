class Trigger:

    CLOCK = 'clock'
    WEATHER = 'weather'

    def __init__(self, type, data):
        self.type = type
        self.data = data
