# make a quiz creator
# pick random question in quiz creator
# user will answer it
# check if the answer is correct

import tkinter as tk
from tkinter import messagebox
import random

def load_question(filename):
    question = []
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            entries = content.split('---\n')
            for entry in entries: 
                lines = entry.strip().split('\n')
                if len(lines) <  6:
                    continue
                q_text = lines[0][len("Question: "):]
                choices = {
                    'a': lines[1][3:],
                    'b': lines[2][3:],
                    'c': lines[3][3],
                    'd': lines[4][3]
                } 
                answer = lines[5][len("Answer) "):].strip().lower()
                questions.append({
                    'question': q_text,
                    'choices': choices,
                    'answer': answer
                })
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {filename} not found." )
        return question

class QuizApp:
    def __init__(self, master):
        self.master = master 
        master.title("Quiz Questions")
        master.geometry("500x400")

        self.question = load_question("quiz_file_gui.txt")
        if not self.question:
            messagebox.showinfo("Info", "No questions available.")
            master.destroy
            return
        
        self.current_question = None

        self.question_label = k.Label(master, text="", wraplength=480,, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.buttons = {}
        for option in ['a', 'b', 'c', 'd']:
            self.buttons[option] = tk.Button(
                master, text="", width=50, command=lambda opt=option: self.check_answer(opt)
            )
            self.buttons[option].pack(pady=5)
        
        self.feedback_label = tk.Label(master, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)

        self.next_button = tk.Button(master, text="Next Question", command=self.load_next_question, state=tk.DISABLED)
        self.next_button.pack(pady=10)

        self.load_next_question()
    
    def load_next_question