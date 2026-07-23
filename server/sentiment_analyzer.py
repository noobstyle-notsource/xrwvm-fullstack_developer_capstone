from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

positive_words = [
    "fantastic", "great", "excellent", "amazing", "wonderful", "good",
    "happy", "best", "love", "recommend", "perfect", "awesome", "superb",
    "friendly", "helpful", "satisfied", "professional", "outstanding",
    "pleasant", "impressed", "comfortable", "reliable", "convenient"
]

negative_words = [
    "terrible", "horrible", "awful", "bad", "worst", "hate",
    "poor", "disappointing", "rude", "slow", "overpriced", "avoid",
    "unhappy", "frustrated", "waste", "broken", "unpleasant",
    "unprofessional", "dishonest", "scam"
]

@app.route('/analyze/<text>')
def analyze(text):
    text_lower = text.lower()

    pos_count = sum(1 for w in positive_words if w in text_lower)
    neg_count = sum(1 for w in negative_words if w in text_lower)

    if pos_count > neg_count:
        sentiment = "positive"
    elif neg_count > pos_count:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return jsonify({"sentiment": sentiment})

@app.route('/')
def home():
    return "Sentiment Analyzer Microservice"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
