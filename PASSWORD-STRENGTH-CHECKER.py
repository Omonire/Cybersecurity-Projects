import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check for digits
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Add at least one digit.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add at least one special character.")

    # Give rating
    if strength == 5:
        return "Strong Password ✅", feedback
    elif strength >= 3:
        return "Moderate Password ⚠", feedback
    else:
        return "Weak Password ❌", feedback

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    result, suggestions = check_password_strength(pwd)
    print("\nStrength:", result)
    if suggestions:
        print("Suggestions to improve:")
        for s in suggestions:
            print("-", s)
