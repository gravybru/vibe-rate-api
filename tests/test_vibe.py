import json
from unittest import TestCase
from unittest import mock
from factory.main_factory import create_app
from tests.mocks.language_service import MockDocumentSentiment, MockSentimentResponse

class BaseSetup(TestCase):
    def setUp(self):
        app = create_app()
        app.config.update({
            "TESTING": True,
        })

        self.app = app
        self.client = app.test_client()

class VibePostTests(BaseSetup):
    def test_400_no_body(self):
        response = self.client.post("/vibe")

        assert response.status_code == 400

    def test_400_malformed_body(self):
        response = self.client.post("/vibe", json={})

        assert response.status_code == 400

    def test_400_malformed_body_2(self):
        response = self.client.post("/vibe", json={"text_content": []})

        assert response.status_code == 400

    @mock.patch("services.sentiment.language_v1.LanguageServiceClient", autospec=True)
    def test_200_correct_response(self, mock_language_service_client):
        # arrange
        sentiment = MockDocumentSentiment(123, 456)
        response = MockSentimentResponse([], "en", sentiment)

        mock_language_service_client().analyze_sentiment.return_value = response

        # act
        response = self.client.post("/vibe", json={"text_content": "the children are crying"})

        body = json.loads(response.get_data())
        data = body["vibe"]

        # assert
        assert response.status_code == 201
        assert data["sentiment_score"] == 123
        assert data["sentiment_magnitude"] == 456
        assert data["language"] == "en"
        assert data["sentences"] == []