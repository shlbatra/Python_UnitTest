from textblob import TextBlob

class sentiment:
    def __init__(self):
        pass

    def extract_sentiment(self,text):
        '''Extract sentiment using textblob. 
        Polarity is within range [-1, 1]'''

        text = TextBlob(text)

        return text.sentiment.polarity
