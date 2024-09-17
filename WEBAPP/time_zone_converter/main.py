from datetime import datetime, timedelta, timezone
from typing import Optional


def utc_to_local(utc_time: str, utc_offset: Optional[float] = None) -> str:
    """
    Converts a given UTC time to local time.

    Args:
        utc_time (str): The time in UTC formatted as "HH:MM".
        utc_offset (Optional[float]): The offset from UTC in hours. If
        not provided, the local system's offset will be used.
    Returns:
        str: Local time formatted as "HH:MM".
    Example:
        >>> print(utc_to_local("17:00", -5))
        12:00
        >>> print(utc_to_local("00:00"))
        19:00
    """
    utc = datetime.strptime(utc_time, "%H:%M").replace(tzinfo=timezone.utc)

    if utc_offset is None:
        local_now = datetime.now().astimezone()
        offset = local_now.utcoffset().total_seconds() / 3600
    else:
        offset = utc_offset
    offset_timedelta = timedelta(hours=offset)
    local_time = utc + offset_timedelta
    return local_time.strftime("%H:%M")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
