class MockSentimentResponse:
    def __init__(self, sentences, language, document_sentiment):
        self.sentences = sentences
        self.language = language
        self.document_sentiment = document_sentiment

class MockDocumentSentiment:
    def __init__(self, score, magnitude):
        self.score = score
        self.magnitude = magnitude