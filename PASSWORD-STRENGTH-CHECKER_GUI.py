from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("At least 8 characters.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add lowercase.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add uppercase.")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Add digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add special char.")

    if strength == 5:
        return "Strong ✅", feedback
    elif strength >= 3:
        return "Moderate ⚠", feedback
    else:
        return "Weak ❌", feedback

class PasswordChecker(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)

        self.add_widget(Label(text="Enter Password:", size_hint=(1, 0.2)))

        self.password_input = TextInput(password=True, multiline=False)
        self.add_widget(self.password_input)

        self.check_button = Button(text="Check Strength", size_hint=(1, 0.3))
        self.check_button.bind(on_press=self.check_password)
        self.add_widget(self.check_button)

        self.result_label = Label(text="", size_hint=(1, 0.2))
        self.add_widget(self.result_label)

        self.feedback_label = Label(text="", size_hint=(1, 0.4))
        self.add_widget(self.feedback_label)

    def check_password(self, instance):
        pwd = self.password_input.text
        result, suggestions = check_password_strength(pwd)
        self.result_label.text = f"Strength: {result}"
        if suggestions:
            self.feedback_label.text = "Suggestions:\n" + "\n".join(suggestions)
        else:
            self.feedback_label.text = "Looks good!"

class PasswordApp(App):
    def build(self):
        return PasswordChecker()

if __name__ == "__main__":
    PasswordApp().run()
