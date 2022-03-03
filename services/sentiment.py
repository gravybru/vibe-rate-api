from google.cloud import language_v1

def sample_analyze_sentiment(text_content):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    document = {
        "content": text_content,
        "type_": language_v1.Document.Type.PLAIN_TEXT,
    }

    response = client.analyze_sentiment(
        request={"document": document, "encoding_type": language_v1.EncodingType.UTF8}
    )

    return response
