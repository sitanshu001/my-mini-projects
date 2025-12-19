import re

def check_password(password):
    if len(password) < 8:
        return "Weak"
    if not re.search(r"[A-Z]", password):
        return "Medium"
    if not re.search(r"[0-9]", password):
        return "Medium"
    if not re.search(r"[@$!%*?&]", password):
        return "Medium"
    return "Strong"

input_password = input("Enter password: ")
print(check_password(input_password))
