import pytest

from skyport import Nasa
from skyport.exceptions import ApiKeyInvalid, IncompatibleParameterFormat, ItemNotFound

invalid_source = Nasa('key-invalid')


def test_exception_of_invalid_key():
    with pytest.raises(ApiKeyInvalid, match='An invalid api_key was supplied.'):
        invalid_source.apod()


def test_exception_of_incompatible_parameter_format(source):
    with pytest.raises(
        IncompatibleParameterFormat,
        match='The provided parameter is incompatible with the expected format.',
    ):
        source.apod('incompatible_parameter_format')


def test_exception_item_not_found(source):
    with pytest.raises(ItemNotFound, match='No item found.'):
        source.neows_lookup(000)
