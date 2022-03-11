from sentiment import sentiment
from textcontain import textcontain
import unittest

class SentimentTestCase(unittest.TestCase):
    obj=sentiment()
    t=textcontain

    def test_extract_sentiment_positive(self):
        text = "I think today will be a great day"
        res = self.obj.extract_sentiment(text)
        assert res > 0

    def test_extract_sentiment_negative(self):
        text = "I do not think this will turn out well"
        res = self.obj.extract_sentiment(text)
        assert res <= 0

    def test_text_contain_word(self):

        word = 'duck'
        sample='This is a duck'
        assert self.t.text_contain_word(word, sample) == True

unittest.main()