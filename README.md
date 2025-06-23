🧠 Quiz Game – True or False?
This is a simple console-based Python project that simulates a True/False quiz game. It presents trivia questions to the user, takes user input, evaluates answers, and tracks the score. The project is designed using Object-Oriented Programming (OOP) principles and includes user interaction through the terminal.

🚀 Features
Loads a list of trivia questions and answers

Presents questions one by one

Accepts user input (True or False)

Checks the answer and updates the score

Displays real-time feedback and running score

Demonstrates class interaction, object creation, and user input handling

📁 Project Structure
📦 quiz-game/
├── data.py              # Contains the trivia question dataset
├── example.py           # Example class demonstrating OOP: follow system between users
├── main.py              # Entry point; runs the quiz
├── question_model.py    # Defines the Question class
├── quiz_brain.py        # Manages quiz logic and flow
🛠️ How It Works
data.py: Stores a list of True/False trivia questions as dictionaries.

question_model.py: Contains the Question class which wraps each question and its correct answer.

quiz_brain.py: Contains the QuizBrain class that controls the quiz loop, handles input/output, checks answers, and maintains score.

main.py: Initializes question objects, creates the quiz instance, and starts the game loop.

example.py: An extra example that demonstrates class relationships and method calls using a social follow feature.

🧪 Example Game Flow
Question 1: A slug's blood is green.
Is that True or False? true
Answer is right
1/ 1

Question 2: The loudest animal is the African Elephant.
Is that True or False? true
Answer is wrong
Correct answer was: False
1/ 2
✅ Requirements
Python 3.x

No external libraries are needed—just run it with the Python interpreter.

▶️ Getting Started
# Clone the repository
git clone https://github.com/yourusername/quiz-game.git
cd quiz-game

# Run the quiz
python main.py
📌 Notes
You can extend the question list or load them dynamically from an API or JSON file.

This is a great foundational project to practice OOP and input handling in Python.

example.py is not part of the quiz game itself but serves as a demonstration of class methods and object relationships.
