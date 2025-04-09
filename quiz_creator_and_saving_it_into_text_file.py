# ask user to input question
# ask for 4 possible answers (a,b,c,d) 
# type letter of correct answer
# write collected data into textfile
# ask question until chose to exit

import tkinter as tk
from tkinter import messagebox

def save_question():
    question = question_entry.get()
    choice_a = entry_a.get()
    choice_b = entry_b.get()
    choice_c = entry_c.get()
    choice_d = entry_d.get()
    answer = correct_answer.get()

    if not all([question, choice_a, choice_b, choice_c, choice_d, answer]):
        messagebox.showwarning("Please fill in all fields.")
        return
    if answer not in ["a", "b", "c", "d"]:
        messagebox.showerror("Correct answer must be one of: a, b, c, d")
        return

