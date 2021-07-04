import pytest

def test_check_user_keyboard():
    phrase = input("Set a phrase until 15 symbols: ")
    assert len(phrase) <= 15
