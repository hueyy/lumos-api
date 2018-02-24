from api.lumos_exception import LumosException


class Trigger:
    CLOCK = 'clock'
    WEATHER = 'weather'
    TEMPERATURE = 'temperature'

    def __init__(self, trigger_data):
        self.id = trigger_data.get('id')
        self.type = trigger_data.get('type')
        self.data = trigger_data.get('data')


def create_trigger(trigger_data):
    from models.triggers.clock_trigger import ClockTrigger
    from models.triggers.weather_trigger import WeatherTrigger
    from models.triggers.temperature_trigger import TemperatureTrigger
    trigger = None
    trigger_type = trigger_data.get('type')
    if trigger_type == Trigger.CLOCK:
        trigger = ClockTrigger(trigger_data)
    elif trigger_type == Trigger.WEATHER:
        trigger = WeatherTrigger(trigger_data)
    elif trigger_type == Trigger.TEMPERATURE:
        trigger = TemperatureTrigger(trigger_data)
    else:
        raise LumosException("invalid trigger type")
    return trigger
