from models.triggers.trigger import Trigger


class WeatherTrigger(Trigger):
    def __init__(self, trigger_data):
        Trigger.__init__(self, trigger_data)
        self.weather_type = trigger_data.get('weather_type')
