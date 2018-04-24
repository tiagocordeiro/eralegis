from eralegis import thelemicdate


def test_return_str():
    td_now = thelemicdate.now()
    assert 'æræ novæ' in td_now
