def view_history():
    try:
        with open("transactions.txt", "r") as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        return []
""" 
######### Learning Signature ######### 
Programmed by: Sean Kyle Anthony L. Panugan
Date Submitted: September 2, 2026
 
Program Description: This program creates a separate module for transaction history.
Reflection: I learned how to create the history module for ATM.
 
AI Usage
[/] No AI Assistance – Completed independently without AI.
[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""