import pytest
from lib.todo import *
# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.

# As a user
# So that I can focus on tasks to complete
# I want to mark tasks as complete and have them disappear from the list.

def test_initially_has_no_Tasks():
    tracker = ToDo()
    assert tracker.incomplete_list() == []
    
def test_add_task():
    tracker = ToDo()
    tracker.add("Walk the dog")
    tracker.add("Walk the cat")
    tracker.add("Feed the fish")
    assert tracker.incomplete_list() == ["Walk the dog","Walk the cat","Feed the fish"]

def test_task_marked_complete():
    tracker = ToDo()
    tracker.add("Walk the dog")
    with pytest.raises(Exception) as e:
        tracker.mark_complete(1)
    assert str(e.value) == "No such task to mark complete"
    assert tracker.incomplete_list() == ["Walk the dog"]
        
    