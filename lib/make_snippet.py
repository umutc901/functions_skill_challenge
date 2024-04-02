def make_snippet(text):
    words = text.split(" ")
    if len(words) >5:
         first_five = words[:5]
         snippet = " ".join(first_five)
         return snippet + "..."
    else:
        return text

def count_words(string):
    word = string.split(" ")
    return len(word)

def reading_time_estimate(wordcount):
    time = wordcount/200
    return time

def grammar_check(grammar):
    return grammar[0].isupper() and grammar[-1] in "!.?"
