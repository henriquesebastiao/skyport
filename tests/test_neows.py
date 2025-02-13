from skyport.types import NeoWs


def test_get_neows(neows_3542519):
    assert isinstance(neows_3542519, NeoWs)


def test_get_neows_orbital_data(neows_3542519):
    assert neows_3542519.orbital_data.data_arc_in_days == 4783
