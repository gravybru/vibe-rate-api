def format_raw_sentiment(response):
    sentences = []

    for sentence in response.sentences:
        summary = {}
        summary["text"] = "{}".format(sentence.text.content)
        summary["sentiment"] = "{}".format(sentence.sentiment.score)
        summary["magnitude"] = "{}".format(sentence.sentiment.magnitude)
        sentences.append(summary)

    return {
        "sentiment_score": response.document_sentiment.score,
        "sentiment_magnitude": response.document_sentiment.magnitude,
        "language": response.language,
        "sentences": sentences,
    }
