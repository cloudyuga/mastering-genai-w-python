from collections import Counter
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for
from langchain_openai import ChatOpenAI
import logging
import os

# Initialize Flask app
app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='hitl_reviews.log', level=logging.INFO)

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize ChatOpenAI
llm = ChatOpenAI(
    temperature=0.7,
    max_tokens=200,
    openai_api_key=OPENAI_API_KEY
)

# File to store feedback counts
FEEDBACK_COUNT_FILE = 'feedback_counts.txt'

def initialize_feedback_counts():
    """Initialize feedback counts file if it doesn't exist."""
    if not os.path.exists(FEEDBACK_COUNT_FILE):
        with open(FEEDBACK_COUNT_FILE, 'w') as file:
            file.write('0,0')  # Initial counts for 'approved' and 'rejected'
    with open(FEEDBACK_COUNT_FILE, 'r') as file:
        counts = file.read().split(',')
        return {
            'approved': int(counts[0]),
            'rejected': int(counts[1])
        }

def update_feedback_counts(feedback_type):
    """Update the feedback counts."""
    counts = initialize_feedback_counts()
    if feedback_type in counts:
        counts[feedback_type] += 1
        with open(FEEDBACK_COUNT_FILE, 'w') as file:
            file.write(f"{counts['approved']},{counts['rejected']}")

# Function to generate text using OpenAI model

def generate_text(prompt):
    response = llm.invoke(prompt)
    return response.content if hasattr(response, "content") else str(response)

# Initialize feedback counter
feedback_counter = Counter(initialize_feedback_counts())

# Route for the home page
@app.route('/')
def home():
    feedback_counts = dict(feedback_counter)
    total_feedback = sum(feedback_counts.values())
    feedback_percentages = {
        'approved': (feedback_counts.get('approved', 0) / total_feedback * 100) if total_feedback > 0 else 0,
        'rejected': (feedback_counts.get('rejected', 0) / total_feedback * 100) if total_feedback > 0 else 0
    }
    return render_template('index.html', feedback_counts=feedback_counts, feedback_percentages=feedback_percentages)

# Route to generate text and display for review
@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    generated_text = generate_text(prompt)
    return render_template('review.html', prompt=prompt, generated_text=generated_text)

# Route to handle review feedback
@app.route('/review', methods=['POST'])
def review():
    prompt = request.form['prompt']
    generated_text = request.form['generated_text']
    feedback = request.form['feedback']
    # Update feedback counter
    update_feedback_counts(feedback)
    feedback_counter.update({feedback: 1})  # Update in-memory counter
    # Log the feedback
    logging.info(f"Prompt: {prompt}")
    logging.info(f"Generated Text: {generated_text}")
    logging.info(f"Feedback: {feedback}")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
