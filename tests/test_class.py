def test_property_rate_limit_remaining(source):
    assert source.rate_limit_remaining >= 0
