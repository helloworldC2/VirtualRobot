from datetime import datetime
from lucenequerybuilder import Q


def datetime_to_timestamp(datetime_obj=datetime.now()):
    """
    If given a `datetime_obj`, converts it to milliseconds since epoch.
    Else, returns the milliseconds between now and the epoch.
    """
    epoch = datetime.utcfromtimestamp(0)
    delta = datetime_obj - epoch
    # Python 3-compatible TimeDelta.total_seconds()
    seconds = (delta.microseconds +
               (delta.seconds + delta.days * 24 * 3600) * 10 ** 6) / 10.0 ** 6
    milliseconds = seconds * 1000
    return int(milliseconds)
