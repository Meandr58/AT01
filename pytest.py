def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Тест 1: Проверка строки, содержащей только гласные
def test_all_vowels():
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5

# Тест 2: Проверка строки без гласных
def test_no_vowels():
    assert count_vowels("bcdfg") == 0
    assert count_vowels("BCDFG") == 0

# Тест 3: Проверка смешанных строк
def test_mixed_string():
    assert count_vowels("Hello World") == 3  # "e", "o", "o"
    assert count_vowels("PyThOn") == 1       # "O"
    assert count_vowels("aEiOuBCDF") == 5    # "a", "E", "i", "O", "u"
