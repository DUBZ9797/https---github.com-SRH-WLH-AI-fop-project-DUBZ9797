from tkinter import Tk, Label, Button, StringVar, OptionMenu
class IntroPage:
    def __init__(self):
        self.root = Tk()
        self.root.title("Quiz Intro")
        self.root.geometry("900x530")
        self.root.configure(bg="#000012")  # Set background color
        # Title label
        Label(self.root, text="Welcome to the Quiz!", font=("Arial", 20), bg="#f0f0f0").pack(pady=20)
        # Category selection
        Label(self.root, text="Select Category:", font=("Arial", 12), bg="#f0f0f0").pack()
        self.category_var = StringVar()
        self.category_var.set("Medicine")  # Default category
        categories = ["Medicine", "Technology"]
        OptionMenu(self.root, self.category_var, *categories).pack(pady=10)
        # Difficulty selection
        Label(self.root, text="Select Difficulty:", font=("Arial", 12), bg="#f0f0f0").pack()
        self.difficulty_var = StringVar()
        self.difficulty_var.set("Easy")  # Default difficulty
        difficulties = ["Easy", "Medium", "Hard"]
        OptionMenu(self.root, self.difficulty_var, *difficulties).pack(pady=10)
        # Start quiz button
        Button(self.root, text="Start Quiz", command=self.start_quiz, bg="#4CAF50", fg="white", font=("Arial", 14), padx=20).pack(pady=20)
        self.root.mainloop()
    def start_quiz(self):
        category = self.category_var.get()
        difficulty = self.difficulty_var.get()
        print("Category:", category)
        print("Difficulty:", difficulty)
if __name__ == "__main__":
    intro_page = IntroPage()

