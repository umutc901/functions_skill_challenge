from lib.single_class import *

# Given a title and contents 
# format returns a formatted entry like:
# My Title: These are the conentss 

def test_formats_with_title_contents():
    diary_entry = DiaryEntry("My Title","Some contents")
    result = diary_entry.format()
    assert result == "My Title: Some contents"

def test_count_words_in_dictionary():
    diary_entry = DiaryEntry("My title","Some Contents")
    result = diary_entry.count_words()
    assert result == 4

def test_reading_time():
    diary_entry = DiaryEntry("My title", "Some Contents")
    result = diary_entry.reading_time(2)
    assert result == 1
    
def test_reading_chunk_with_two_wpm_and_two_minutes():
    diary_entry = DiaryEntry("my title","one two three four five six")
    result = diary_entry.reading_chunk(2, 2)
    assert result == "one two three four"


