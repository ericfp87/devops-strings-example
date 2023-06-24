from string_stadardization import stringstd


def test_full_name():
    name = "Eric Ferreira"
    std_name = stringstd.standardize(name)
    assert len(std_name.split(' ')) > 1
