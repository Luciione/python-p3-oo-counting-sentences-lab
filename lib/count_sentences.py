#!/usr/bin/env python3

class MyString:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the string into sentences using periods as separators
        sentences = self.value.split('.')
        
        # Count the non-empty sentences
        count = 0
        for sentence in sentences:
            if sentence.strip():  # Check if the sentence is not empty
                count += 1
        return count
