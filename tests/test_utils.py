from skyport._utils import valid_date


def test_valid_date_with_invalid_date():
    assert not valid_date('2025-02-30')


def test_valid_date_with_valid_date():
    assert valid_date('2025-02-13')
