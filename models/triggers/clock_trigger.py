from models.triggers.trigger import Trigger

SCHEDULE_TYPES = [

]


class ClockTrigger(Trigger):

    EVERY_DAY = 'every_day'
    EVERY_MONDAY = 'every_monday'
    EVERY_TUESDAY = 'every_tuesday'
    EVERY_WEDNESDAY = 'every_wednesday'
    EVERY_THURSDAY = 'every_thursday'
    EVERY_FRIDAY = 'every_friday'
    EVER_SATURDAY = 'every_saturday'
    EVERY_SUNDAY = 'every_sunday'
    EVERY_HOUR = 'every_hour'

    ONCE = 'once'

    def __init__(self, trigger_data):
        Trigger.__init__(self, trigger_data)
        self.schedule = trigger_data.get('schedule')

        requires_time = self.schedule in [
            ClockTrigger.EVERY_DAY, ClockTrigger.EVERY_MONDAY,
            ClockTrigger.EVERY_TUESDAY, ClockTrigger.EVERY_WEDNESDAY,
            ClockTrigger.EVERY_THURSDAY, ClockTrigger.EVERY_FRIDAY,
            ClockTrigger.EVERY_SATURDAY, ClockTrigger.EVERY_SUNDAY
        ]
        if requires_time:
            self.time = trigger_data.get('time')

        requires_minute = self.schedule == ClockTrigger.EVERY_HOUR
        if requires_minute:
            self.minute = trigger_data.get('minute')

        requires_timestamp = self.schedule == ClockTrigger.ONCE
        if requires_timestamp:
            self.timestamp = trigger_data.get('timestamp')
