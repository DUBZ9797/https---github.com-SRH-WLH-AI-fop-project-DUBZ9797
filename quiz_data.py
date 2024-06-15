import json
import random
 
# Assuming 'questions.json' is in the same directory as this script
filename = 'GUI-Quiz-Tkinter-master\question1.json'
 
try:
    with open(filename, 'r') as file:
        data = json.load(file)

    #shuffle the questions to get a random selection
    random.shuffle(data)

    #take the first 5 questions
    selected_questions = data[:5]

    print(selected_questions)
    question_data = selected_questions
except FileNotFoundError:
    print(f"File not found: {filename}")
except Exception as e:
    print(f"An error occurred: {e}")



