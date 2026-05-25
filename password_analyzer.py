import tkinter as tk
from tkinter import messagebox
import random
import string

def check_password_strength(password):
    score = 0
    remarks = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Use at least 8 characters")

    # Uppercase Check
    if any(char.isupper() for char in password):
        score += 1
    else:
        remarks.append("Add uppercase letters")

    # Lowercase Check
    if any(char.islower() for char in password):
        score += 1
    else:
        remarks.append("Add lowercase letters")

    # Digit Check
    if any(char.isdigit() for char in password):
        score += 1
    else:
        remarks.append("Add numbers")

    # Special Character Check
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(char in special_chars for char in password):
        score += 1
    else:
        remarks.append("Add special characters")

    # Strength Result
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, remarks

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(12))
    return password

def analyze_password():
    password = entry.get()

    if not password:
        messagebox.showwarning("Warning", "Please enter a password")
        return

    strength, remarks = check_password_strength(password)

    result_label.config(text=f"Password Strength: {strength}")

    if remarks:
        suggestion_text = "\n".join(remarks)
        suggestions_label.config(text=f"Suggestions:\n{suggestion_text}")
    else:
        suggestions_label.config(text="Excellent Password!")

def suggest_password():
    strong_pass = generate_strong_password()
    messagebox.showinfo("Suggested Password", strong_pass)

# GUI Window
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("450x350")
root.config(bg="#f0f4f7")

title = tk.Label(root, text="Password Strength Analyzer",
                 font=("Arial", 18, "bold"),
                 bg="#f0f4f7")
title.pack(pady=15)

entry = tk.Entry(root, width=35, show="*", font=("Arial", 12))
entry.pack(pady=10)

analyze_btn = tk.Button(root, text="Analyze Password",
                        command=analyze_password,
                        bg="#4CAF50",
                        fg="white",
                        font=("Arial", 11, "bold"))
analyze_btn.pack(pady=10)

suggest_btn = tk.Button(root, text="Suggest Strong Password",
                        command=suggest_password,
                        bg="#2196F3",
                        fg="white",
                        font=("Arial", 11, "bold"))
suggest_btn.pack(pady=5)

result_label = tk.Label(root, text="",
                        font=("Arial", 14, "bold"),
                        bg="#f0f4f7")
result_label.pack(pady=15)

suggestions_label = tk.Label(root, text="",
                             font=("Arial", 11),
                             bg="#f0f4f7",
                             justify="left")
suggestions_label.pack()

root.mainloop()