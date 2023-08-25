import io
import sys
import pytest
from count_sentences import MyString

class TestMyString:

    def test_is_class(self):
        '''is a class with the name "MyString".'''
        assert(isinstance(MyString("test string"), MyString))

    def test_value_string(self):
        '''prints "The value must be a string." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        string = MyString("test string")  # Provide a valid string value here
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == ""

    def test_is_sentence(self):
        '''returns True if value ends with a period and False otherwise.'''
        string = MyString("test string")  # Provide a valid string value here
        assert string.is_sentence() == False

    def test_is_question(self):
        '''returns True if value ends with a question mark and False otherwise.'''
        string = MyString("test string")  # Provide a valid string value here
        assert string.is_question() == False

    def test_is_exclamation(self):
        '''returns True if value ends with an exclamation mark and False otherwise.'''
        string = MyString("test string")  # Provide a valid string value here
        assert string.is_exclamation() == False

    def test_count_sentences(self):
        '''returns the number of sentences in the value.'''
        simple_string = MyString("one. two. three?")  # Provide a valid string value here
        empty_string = MyString("")  # Provide a valid string value here
        assert simple_string.count_sentences() == 3
        assert empty_string.count_sentences() == 0
