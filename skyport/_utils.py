from datetime import datetime


def valid_date(date: str) -> bool:
    """Checks if a date is valid according to [ISO 8601](https://pt.wikipedia.org/wiki/ISO_8601).

    Args:
        date (str): Date in string.

    Returns:
        bool: True or False, depending on whether it is valid or not.
    """
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False
