from datetime import date

import pytest

from skyport.exceptions import InvalidDateFormat
from skyport.types import Apod


def test_apod_title_is_str(apod_2024_12_30):
    assert isinstance(apod_2024_12_30.title, str)


def test_apod_date_is_instance_of_date(apod_2024_12_30):
    assert isinstance(apod_2024_12_30.date, date)


def test_apod_explanation_is_str(apod_2024_12_30):
    assert isinstance(apod_2024_12_30.explanation, str)


def test_apod_media_type_is_str(apod_2024_12_30):
    assert isinstance(apod_2024_12_30.media_type, str)


def test_apod_url_is_str(apod_2024_12_30):
    assert isinstance(apod_2024_12_30.url, str)


def test_apod_service_version_is_str(apod_2024_12_30):
    assert isinstance(apod_2024_12_30.service_version, str)


def test_apod_copyright_is_none(apod_2025_02_12):
    assert apod_2025_02_12.copyright is None


def test_apod_copyright_is_str(apod_2024_12_30):
    assert isinstance(apod_2024_12_30.copyright, str)


def test_get_apod_timeline_with_str_parameters(source):
    apods = source.apod_timeline('2024-01-01', '2024-01-03')
    assert isinstance(apods, list)


def test_get_apod_with_str_parameter(source):
    apod = source.apod('2025-02-12')
    assert isinstance(apod, Apod)


def test_get_apod_with_date_parameter(source):
    apod = source.apod(date(2025, 2, 12))
    assert isinstance(apod, Apod)


def test_get_apod_timeline_with_date_parameters(source):
    apods = source.apod_timeline(date(2024, 1, 1), date(2024, 1, 3))
    assert isinstance(apods, list)


def test_get_apod_random(source):
    apods = source.apod_random(5)
    assert isinstance(apods, list)


def test_apod_with_invalid_date_string(source):
    with pytest.raises(
        InvalidDateFormat,
        match='The 2025-02-30 date is invalid, the date must follow ISO 8601.',
    ):
        source.apod('2025-02-30')


def test_apod_time_line_with_invalid_start_date(source):
    with pytest.raises(
        InvalidDateFormat,
        match='The 2025-02-30 date is invalid, the date must follow ISO 8601.',
    ):
        source.apod_timeline('2025-02-30', '2025-03-01')


def test_apod_time_line_with_invalid_end_date(source):
    with pytest.raises(
        InvalidDateFormat,
        match='The 2025-02-30 date is invalid, the date must follow ISO 8601.',
    ):
        source.apod_timeline('2025-01-01', '2025-02-30')
