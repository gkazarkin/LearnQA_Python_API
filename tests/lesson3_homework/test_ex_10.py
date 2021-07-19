import pytest
@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_check_user_keyboard():
    phrase = input("Set a phrase until 15 symbols: ")
    assert len(phrase) <= 15
