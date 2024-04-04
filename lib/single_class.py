class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        
    def format(self):
        return f'{self.title}: {self.contents}' 

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        words = self.format().split()
        print(words)
        return len(words)

    def reading_time(self, wpm):
        contents_words_count = len(self.contents.split())
        return contents_words_count/wpm
    
    def reading_chunk(self, wpm, minutes):
        words_user_can_read = wpm*minutes
        words = self.contents.split()
        chunk_words = words[:words_user_can_read]
        return " ".join(chunk_words)
    
