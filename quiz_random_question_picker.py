# make a quiz creator
# pick random question in quiz creator
# user will answer it
# check if the answer is correct

import tkinter as tk
from tkinter import messagebox
import random

def load_questions(filename):
    questions = []
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            entries = content.split('---\n')
            for entry in entries:
                lines = entry.strip().split('\n')
                if len(lines) < 6:
                    continue  # skip incomplete entries
                q_text = lines[0][len("Question: "):]
                choices = {
                    'a': lines[1][3:],
                    'b': lines[2][3:],
                    'c': lines[3][3:],
                    'd': lines[4][3:]
                }
                answer = lines[5][len("Answer) "):].strip().lower()
                questions.append({
                    'question': q_text,
                    'choices': choices,
                    'answer': answer
                })
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {filename} not found.")
    return questions

class QuizApp:
    def __init__(self, master):
        self.master = master
        master.title("Quiz Questions")
        master.geometry("500x400")

        self.questions = load_questions("quiz_file_gui.txt")
        if not self.questions:
            messagebox.showinfo("Info", "No questions available.")
            master.destroy()
            return

        self.current_question = None

        self.question_label = tk.Label(master, text="", wraplength=480, font=("Arial", 14))
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

    def load_next_question(self):
        self.current_question = random.choice(self.questions)
        q = self.current_question

        self.question_label.config(text=q['question'])
        for opt in ['a', 'b', 'c', 'd']:
            self.buttons[opt].config(text=f"{opt}) {q['choices'][opt]}", state=tk.NORMAL)

        self.feedback_label.config(text="")
        self.next_button.config(state=tk.DISABLED)

    def check_answer(self, selected):
        correct = self.current_question['answer']
        if selected == correct:
            self.feedback_label.config(text="✅ Correct!", fg="green")
        else:
            correct_text = self.current_question['choices'][correct]
            self.feedback_label.config(
                text=f"❌ Incorrect. Correct answer: {correct}) {correct_text}", fg="red"
            )

        for btn in self.buttons.values():
            btn.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

# Run the quiz app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()