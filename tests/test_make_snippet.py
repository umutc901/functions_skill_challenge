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
    
def test_estimated_reading_time():
    result = reading_time_estimate(500)
    assert result == 2.5
def test_reading_time_2():    
    result = reading_time_estimate(700)
    assert result == 3.5

def test_if_begin_with_capital():
    result = grammar_check("This sentence begins with a capital and ends with proper punctuation.")
    assert result == True