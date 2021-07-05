import requests
from lxml import html
import pytest

page = requests.get("http://example.com").text
tree = html.fromstring(page)
text = tree.xpath("//p//text()")
print(text)

"""C помощью requests получаешь страничку и парсишь с помощью xpath - очень удобно покрывать статические странички, быстрее чем selenium работает )"""

# 2
"""В Python есть возможность декларировать тип параметра и возвращаемого значения для функции.
Тут мы на вход ждем два параметра типа str (то есть строки). А возвращать обязуемся list (список).
Это порой удобно, чтобы Python нам подсказывал, если вдруг мы передаем или возвращаем что-то не то."""
def get_user(email: str, password: str) -> list:
    pass

# 3
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
