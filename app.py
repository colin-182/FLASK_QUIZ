from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name___)

app.secret_key = "change-this-to-something-secret"

# Quiz questions
# A list of dictionaries. Each dictionary is one questions.
# "question" = the text shown to the user
# "options" = the four answer choices (a list)
# "answer" = the EXACT string that must match the correct option
QUESTIONS = [
    {
        "question": "What is the capital city of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris",
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": ["5", "6", "7", "8"],
        "answer": "6",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars",
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Arctic" "Pacific"],
        "answer": "Pacific",
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Van Gogh", "Picasso", "Da Vinci", "Rembrandt"],
        "answer": "Da Vinci",
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["O2", "CO2", "H2O", "HO"],
        "answer": "H2O",
    },
    {
        "question": "In what year did World War II end?",
        "options": ["1943", "1944", "1945", "1946"],
        "answer": "1945",
    },
    {
        "question": "What is the fastest land animal?",
        "options": ["Lion", "Horse", "Cheetah", "Greyhound"],
        "answer": "Cheetah",
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["5", "6", "7", "8"],
        "answer": "7",
    },
    {
        "question": "What language has the most native speakers in the world?",
        "options": ["English", "Spanish", "Madarin", "Hindi"],
        "answer": "Mandarin",
    },
]

# Route 1: Home page
@app.route("/")
def home():
    return render_template("index.html")

# Route 2: Starting the quiz
# This should reset everything in the session so the quiz always starts fresh
# url_for ("question") builds the URL for the "question" function below
@app.route("/start")
def start():
    session["question_index"] = 0
    session["score"] = 0
    session["answers"] -[]
    return redirect(url_for("question"))

# Route 3: Show the current question
@app.route("/question")
def question():
    index = session.get("question_index", 0)
    if index >= len(QUESTIONS):
        return redirect(url_for("results"))

# Get just the current question dictionary from the list
    current_question = QUESTIONS[index]

# Passing data to the template using keyword arguments
# 'number' is used to show "Question 1 of 10" etc.
    return render_template(
        "quiz.html",
        question=current_question,
        number=index + 1,
        total=len(QUESTIONS),
    )

# Route 4: Handling the users answer
# POST should accept form of submission, not page visits
@app.route("/answer", methods=["POST"])
def answer():
    index = session.get("question_index", 0)
    current = QUESTIONS[index]
    chosen = request.form.get("choice")

    # Check if the chosen answer matches correct answer
    is_correct = chosen == current["answer"]
    if is_correct:
        session["score"] += 1

    # Record this answer so we can show a review on results page
    session["answers"] = session.get("answers", []) + [{
        "question": current["question"],
        "chosen": chosen,
        "correct": current["answer"],
        "right": is_correct,
    }]

    # Move to the next question
    session["question_index"] = index + 1

