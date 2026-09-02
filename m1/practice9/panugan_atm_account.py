class Account:
    def __init__(self, name, starting_balance):
        self.account_name = name
        self._balance = starting_balance

    def check_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        return False    
""" 
######### Learning Signature ######### 
Programmed by: Sean Kyle Anthony L. Panugan
Date Submitted: September 2, 2026
 
Program Description: This program adds a withdraw function to the account class.
Reflection:  I learned how classes are efficient for assigning
attributes for every object.
 
AI Usage
[/] No AI Assistance – Completed independently without AI.
[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""