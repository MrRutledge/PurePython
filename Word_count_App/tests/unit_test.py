import pytest

from app.word_counter import find_top_word 
#from app import word_count
    

@pytest.mark.talk_run   
def test_find_top_word():
    words = ['foo', 'bar','bat','bax','foo','baz','foo']

    result = find_top_word(words)
    assert result[0] == "foo"
    assert result[1] == 3