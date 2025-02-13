from skyport.types import NeoWs


def test_get_neows(neows_3542519):
    assert isinstance(neows_3542519, NeoWs)
