# FLASK_QUIZ
UCD Module 3 - Python Assignment 

HTML checker - No errors or warnigns to show 10/4/26
JSHINT checker - 1 warning - Use the function form of "use strict". Old ES5 concern that shouldn't apply to modern Java. 10/4/26
CSS checker - many warnings but seem to be more about their limitations. VARs are dynamic and known by browser at runtime when it reads :root block. Validator is a static tool so when it reads code it physically can't check check dynamic values. 10/4/26


Overview
This project was built step by step as a learning exercise in Flask web development. The initial plan was to build a portfolio website, but after consideration a quiz app was chosen as a better demonstration of Flask's core strengths — routing, sessions, form handling, and dynamic templating.

Features
10 general knowledge questions with 4 multiple choice answers each
One question per page with a live progress bar
Score tracking using Flask sessions
Detailed results page with a per-question answer review
Feedback form with star rating and on-screen success notification (no page reload)
Fully responsive design — works on mobile and desktop
Deployed live on Render.com


Project Structure
FLASK_QUIZ/
├── app.py                  # Flask application, routes and quiz logic
├── requirements.txt        # Python dependencies
├── .gitignore              # Excludes venv and cache from Git
├── templates/
│   ├── base.html           # Shared layout (nav, footer, CSS/JS links)
│   ├── index.html          # Home page
│   ├── quiz.html           # Question page
│   ├── results.html        # Score and answer review page
│   └── feedback.html       # Feedback form page
└── static/
    ├── css/
    │   └── style.css       # All styles
    └── js/
        └── script.js       # All interactivity

Step-by-Step Build Process
Step 1 — Environment Setup
Before writing any code, the development environment was configured:

Created the project folder and subdirectories (templates/, static/css/, static/js/)
Created and activated a Python virtual environment using python3 -m venv venv
Installed dependencies: pip install flask gunicorn python-dotenv
Created a .gitignore to exclude venv/, __pycache__/, and .env
Saved dependencies with pip freeze > requirements.txt
Initialised a GitHub repository and linked it to the local project

Step 2 — app.py
The core Flask application was built first, before any HTML. This file contains:

The Flask app object and secret key for sessions
The full list of 10 quiz questions stored as a list of dictionaries
Five routes: / (home), /start (reset session), /question (show current question), /answer (process answer), /results (show final score), and /feedback (feedback form)
Flask sessions to track question_index, score, and answers across page loads

Step 3 — base.html
A shared base template was created that all other pages extend. This avoids repeating the nav, footer, and CSS/JS link tags on every page. Key concepts used:

{% block content %}{% endblock %} as the slot for each page's unique content
url_for() for all internal links and static file references

Step 4 — index.html
The home page was built as the first child template. It extends base.html and fills the content block with a welcome card, quiz stats, and a Start Quiz button linking to the /start route.
Step 5 — quiz.html
The question page receives question, number, and total variables from app.py. Key features:

A progress bar whose width is calculated using Jinja2 arithmetic: {{ (number / total * 100) | int }}%
Answer buttons built using a Jinja2 {% for %} loop over question.options
Each button is a form submit input with name="choice" and value="{{ option }}" so Flask can read the selection with request.form.get("choice")
A, B, C, D labels generated using {{ "ABCD"[loop.index0] }}

Step 6 — results.html
The results page displays the final score and a full answer review. Key features:

Conditional emoji and feedback message using Jinja2 {% if / elif / else %} based on score percentage
A review list built by looping over the answers list passed from app.py
Green/red styling applied conditionally using {% if item.right %}review-item--correct{% else %}review-item--wrong{% endif %}

Step 7 — feedback.html
A fifth page added to meet the project requirement of five HTML files and to add genuine functionality. Features:

Name, star rating, and comments fields
Star rating built with radio inputs styled as clickable stars using pure CSS
On submission, JavaScript uses fetch() to post the form in the background and show a success notification without reloading the page

Step 8 — style.css
A full stylesheet was written with an editorial dark theme using purple accents. Key techniques:

CSS custom properties (variables) defined in :root for consistent theming throughout
clamp() for fluid responsive typography that scales with screen size
@keyframes animations for page load effects and floating background blobs
CSS Grid for the two-column answer button layout, falling back to one column on mobile
The reversed flex-direction trick for the star rating so CSS sibling selectors work left to right

Step 9 — script.js
JavaScript was added last since the app works without it. Four features were implemented:

Nav scroll effect — darkens the navbar background as the user scrolls
Answer button lock — disables all buttons except the clicked one on submit to prevent double submissions
Staggered results animation — each answer review row animates in with a sequential delay using setTimeout
Feedback form AJAX — submits the feedback form using fetch() and shows a success message without a page reload
Keyboard support — allows keyboard users to select answers with Enter or Space

Step 10 — Deployment to Render.com
The app was deployed as a live web service:

A render.yaml config file was added specifying the build and start commands
Gunicorn was used as the production WSGI server instead of Flask's built-in development server
debug=False was set in app.py before deployment


Difficulties Faced
Python Version Conflict
The Mac had Python 3.14 installed by default which has a known bug where pip is not properly available inside virtual environments. After several failed attempts, the issue was resolved by installing Python 3.12 (a stable version) via Homebrew and using that to create the virtual environment.
Port 5000 Conflict on Mac
Flask defaults to port 5000, which conflicts with Apple's AirPlay Receiver on macOS Monterey and later. This caused a 403 Access Denied error when first trying to view the app in the browser. It was resolved by disabling AirPlay Receiver in System Settings.
Jinja2 Template Typos
Several small typos in template files caused 500 errors that only appeared at runtime:

__name___ (three underscores) instead of __name__ in app.py
js/script.js without quotes inside url_for() in base.html
rage(1, 6) instead of range(1, 6) in feedback.html
request.methods instead of request.method in the feedback route

Each was diagnosed by reading the Render.com logs which pinpoint the exact file and line number of the error.
Answer Button Double Submit Bug
The original JavaScript disabled all answer buttons immediately on click, including the clicked button itself. Since disabled form buttons do not submit their value, Flask received None for the answer and the quiz got stuck on the first question. This was only noticeable on Render (not locally) due to the slight network latency. The fix was to disable all buttons except the one that was clicked, so its value still submits correctly.
Feedback Page Layout
Several issues in feedback.html caused the card layout to break — a missing form__group wrapper around the star rating, a stray extra </div> closing the card too early, a missing CSS class on the textarea, and a typo on the success message div ID (sucessMessage instead of successMessage). These were identified by comparing the broken HTML structure against the intended layout.