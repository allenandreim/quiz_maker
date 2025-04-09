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
    
    quiz_entry = (
        f"Question: {question}\n"
        f"a) {choice_a}\n"
        f"b) {choice_b}\n"
        f"c) {choice_c}\n"
        f"d) {choice_d}\n"
        f"Answer) {answer}\n"
        f"---\n"
    )
    with open("quiz_file_gui.txt", "a") as file:
        file.write(quiz_entry)

    question_entry.delete(0, tk.END)
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    entry_d.delete(0, tk.END)
    correct_answer.delete(0, tk.END)

    messagebox.showinfo("Saved", "Question saved succesfully.")

root = tk.Tk()
root.title("Quiz Maker")
root.geometry("400x450")

tk.Label(root, text="Enter your quiz question:").pack(pady=5)
question_entry = tk.Entry(root, width=50)
question_entry.pack()

tk.Label(root, text="Choice a:").pack()
entry_a = tk.Entry(root, width=50)
entry_a.pack()

tk.Label(root, text="Choice b:").pack()
entry_b = tk.Entry(root, width=50)
entry_b.pack()

tk.Label(root, text="Choice c:").pack()
entry_c = tk.Entry(root, width=50)
entry_c.pack()

tk.Label(root, text="Choice d:").pack()
entry_d = tk.Entry(root, width=50)
entry_d.pack()

tk.Label(root, text="Correct answer (a,b,c,d):").pack(pady=5)
correct_answer = tk.Entry(root, width=10)
correct_answer.pack()

tk.Button(root, text="Save Question", command=save_question, bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=20)

root.mainloop()