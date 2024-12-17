# Quizzer
A simple and interactive quiz web application built with Python and Django. Quizzer allows users to customize their quiz experience by selecting the difficulty level, number of questions, and a timer. At the end of the quiz, users can view their results and restart the quiz.

# 🚀 Live Demo
Try the live application here:
🔗 Quizzer - https://quizzer-one-iota.vercel.app/

# 🛠 Features
Three Difficulty Levels: Easy, Medium, Hard.
Customizable Quiz: Select the number of questions and a timer.
Interactive UI: Start quiz button, options for answering, and result display.
Results Page: View the total number of correct answers.
Restart Option: Option to play the quiz again with new questions.


# 💻 Tech Stack
Backend: Python, Django
Frontend: HTML, CSS
Deployment: Vercel

# 📦 Installation
To run this project locally, follow these steps:

Clone the Repository
git clone https://github.com/yourusername/quizzer.git
cd quizzer

Create a Virtual Environment
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

Install Dependencies
pip install django

Run Migrations
python manage.py makemigrations
python manage.py migrate

Add Quiz Questions
Use Django's admin panel or shell to populate the database with quiz questions.

Run the Development Server
python manage.py runserver
Open the app in your browser: http://127.0.0.1:8000/

