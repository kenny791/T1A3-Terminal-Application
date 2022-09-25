from lookup import search
import pytest

inputs=iter(['Egypt', 'France', 'Greece'])

def fake_input(prompt):
    return next(inputs)

class TestSearch():
    def test_valid(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        assert search()  != '\nCountry not found, please enter another country\n'
        assert search()  != '\nCountry not found, please enter another country\n'
        assert search()  != '\nCountry not found, please enter another country\n'








from capitals import answers
inputs2=iter(['a','a'])

def fake_input2(prompt):
    return next(inputs2)

class TestAnswers():
    def test_valid2(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input2)
        assert len(answers())  == 4
        assert all(x != 0 for x in answers())


