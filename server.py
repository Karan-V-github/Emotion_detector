"""
Flask server for Emotion Detection application.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the index page with the text input and button.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Handle GET requests for emotion detection.
    Extracts the text from the query parameter, calls the emotion_detector
    function, and returns a formatted response string.
    If no text is provided or the API response is invalid,
    an error message is returned instead.
    """
    statement = request.args.get("textToAnalyze")
    if not statement:
        return "Invalid text! Please try again!"

    response = emotion_detector(statement)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant = response["dominant_emotion"]

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

    return formatted_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
