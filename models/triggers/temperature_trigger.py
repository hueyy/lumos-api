from models.triggers.trigger import Trigger


class TemperatureTrigger(Trigger):
    LESS_THAN = 'less_than'
    GREATER_THAN = 'greater_than'
    def __init__(self, trigger_data):
        Trigger.__init__(self, trigger_data)
        self.temperature = trigger_data.get('temperature')
        self.direction = trigger_data.get('direction')
