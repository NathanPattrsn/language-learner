from flask import Flask, request, jsonify
from flask_cors import CORS
from lessons import get_recommended_lessons
from pronunciation import analyze_user_pronunciation
from chatbot import get_chatbot_response

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests from React frontend

# Route to fetch personalized lessons
@app.route('/api/recommended-lessons', methods=['GET'])
def recommended_lessons():
    lessons = get_recommended_lessons()
    return jsonify(lessons)

# Route to analyze pronunciation
@app.route('/api/analyze-pronunciation', methods=['POST'])
def analyze_pronunciation():
    data = request.json
    text = data.get('text')
    feedback = analyze_user_pronunciation(text)
    return jsonify({'feedback': feedback})

# Route for chatbot interaction
@app.route('/api/chatbot', methods=['POST'])
def chat():
    user_input = request.json.get('message')  # Get user input from request
    response = get_chatbot_response(user_input)  # Call your chatbot function
    return jsonify({'response': response})  # Return the response as JSON

if __name__ == '__main__':
    app.run(debug=True)
