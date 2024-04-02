from lib.make_snippet import *

def test_if_empty_string_return_empty_string():
    result = make_snippet("")
    assert result == ""

def test_five_word_string():
    result = make_snippet("one two three four five")
    assert result == "one two three four five"
def test_six_word_string():
    result = make_snippet("one two three four five six")
    assert result == "one two three four five..."

def test_count_words():
    result = count_words("one two three four five six seven")
    assert result == 7