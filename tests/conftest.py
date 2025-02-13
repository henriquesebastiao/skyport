import os

import pytest

from skyport import Nasa


@pytest.fixture(scope='session')
def source():
    return Nasa(os.getenv('NASA_API_KEY_TEST', 'DEMO_KEY'))


@pytest.fixture(scope='session')
def apod_2024_12_30(source):
    return source.apod('2024-12-30')


@pytest.fixture(scope='session')
def apod_2025_02_12(source):
    """APOD without hdurl and copyright."""
    return source.apod('2025-02-12')


@pytest.fixture(scope='session')
def neows_3542519(source):
    return source.neows_lookup(3542519)
