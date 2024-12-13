class CloudWatchAlarmException(Exception):
    def __init__(self, message="Intended CloudWatch Alarm Trigger"):
        self.message = message
        super().__init__(self.message)


def handler(event, context):
    raise CloudWatchAlarmException("Intended CloudWatch Alarm Trigger")
