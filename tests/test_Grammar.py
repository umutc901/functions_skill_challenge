from lib.Grammar import *

def test_check_first_letter_capital_is_true():
    text_entry = GrammarStats()
    result = text_entry.check("This is a sentence!")
    assert result == True
    
def test_check_end_punctuation_is_true():
    text_entry = GrammarStats()
    result = text_entry.check("This is a sentence.")
    assert result == True

def test_check_percentage():
    grammar_stats = GrammarStats()
    assert grammar_stats.percentage_good() == 0
    grammar_stats.check("This is a sentence!")
    grammar_stats.check("Another sentence.")
    grammar_stats.check("Yet another sentence!")
    # Now, 100% of the checked texts passed the check
    assert grammar_stats.percentage_good() == 100

    # Check some texts that don't pass the check
    grammar_stats.check("not starting with a capital letter.")
    grammar_stats.check("nor ending with punctuation")
    # Now, only 3 out of 5 texts passed the check, so the percentage should be 60
    assert grammar_stats.percentage_good() == 60

