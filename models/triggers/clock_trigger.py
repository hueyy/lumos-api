from models.triggers.trigger import Trigger


class ClockTrigger(Trigger):
    def __init__(self, trigger_data):
        Trigger.__init__(self, trigger_data)
        self.schedule = trigger_data.get('schedule')
        self.time = trigger_data.get('time')
