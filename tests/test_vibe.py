import json
from unittest import mock
from tests.base import BaseSetup
from tests.mocks.language_service import MockDocumentSentiment, MockSentimentResponse

from tests.utils_test import sign_in_test_user

class VibePostTests(BaseSetup):

    def setUp(self):
        super().setUp()

        sign_in_response = sign_in_test_user()
        jwt = sign_in_response["idToken"]
        self.jwt = jwt

    def test_401_no_token(self):
        response = self.client.post("/vibe")

        body = json.loads(response.get_data())

        assert body["message"] == 'No authorization token provided'
        assert response.status_code == 401

    def test_401_bad_token(self):
        response = self.client.post("/vibe", headers={"authorization": "gluten"})

        body = json.loads(response.get_data())

        assert body["message"] == 'Invalid authorization token provided'
        assert response.status_code == 401

    def test_400_no_body(self):
        response = self.client.post("/vibe", headers={"authorization": self.jwt})

        assert response.status_code == 400

    def test_400_malformed_body(self):
        response = self.client.post("/vibe", json={}, headers={"authorization": self.jwt})

        assert response.status_code == 400

    def test_400_malformed_body_2(self):
        response = self.client.post("/vibe", json={"text_content": []}, headers={"authorization": self.jwt})

        assert response.status_code == 400

    @mock.patch("services.sentiment.language_v1.LanguageServiceClient", autospec=True)
    def test_200_correct_response(self, mock_language_service_client):
        # arrange
        sentiment = MockDocumentSentiment(123, 456)
        response = MockSentimentResponse([], "en", sentiment)

        mock_language_service_client().analyze_sentiment.return_value = response

        # act
        response = self.client.post("/vibe", json={"text_content": "the children are crying"}, headers={"authorization": self.jwt})

        body = json.loads(response.get_data())
        data = body["vibe"]

        # assert
        assert response.status_code == 201
        assert data["sentiment_score"] == 123
        assert data["sentiment_magnitude"] == 456
        assert data["language"] == "en"
        assert data["sentences"] == []