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

