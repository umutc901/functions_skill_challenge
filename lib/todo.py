# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.

# As a user
# So that I can focus on tasks to complete
# I want to mark tasks as complete and have them disappear from the list.
class ToDo():
    def __init__(self):
        self.list = []
        
    def add(self,task):
        self.list.append(task)
        
    def incomplete_list(self):
        return self.list
    
    def mark_complete(self,index):
        if index < 0 or index >= len(self.list):
            raise Exception('No such task to mark complete')
        del self.list[index]
        
   
