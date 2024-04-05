class GrammarStats:
    def __init__(self):
        self.total_checks = 0
        self.passed_checks = 0
    
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if text[0].isupper() and text[-1] in "!,.?":
            self.passed_checks += 1
            self.total_checks +=1
            return True
        else:
            self.total_checks +=1
            return False
        
    def percentage_good(self):
        # Returns:
        #   int: the perpytesentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.total_checks == 0:
            return 0
        else:
            percentage = int((self.passed_checks / self.total_checks) * 100)
            return percentage
        