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