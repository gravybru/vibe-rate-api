from flask_restful import Resource
from flask import request
from services.format import format_raw_sentiment
from services.sentiment import sample_analyze_sentiment

error = {"error": "'text_content' missing on request body"}

class VibeRateController(Resource):
    def post(self):
        try:
            if (request.get_json() is None): return error, 400

            text_content = request.get_json()["text_content"]

            if len(text_content) == 0: return error, 400

            raw = sample_analyze_sentiment(text_content)
            
            response = format_raw_sentiment(raw)

            return {"vibe": response}, 201

        except KeyError:
            return error, 400
