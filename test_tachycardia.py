import pytest


@pytest.mark.parametrize("input, expected", [
    ("tachycardic", True),
    ("TAchycar", False),
    ])
def test_tachycardic(input, expected):
    from tachycardia import is_tachycardic
    answer = is_tachycardic(input)
    assert answer == expected
