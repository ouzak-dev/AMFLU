import customtkinter as ctk
from tkinter import messagebox
from app.database import open_db_connection, close_db_connection
from app.database.db_setup import UserManager
from .. import hash_password

class Signup(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app

        # Configure the frame layout
        self.configure(fg_color="#f2f2f2")  # Light gray background
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(list(range(5)), weight=1)

        # Add a title to the signup screen
        self.label_title = ctk.CTkLabel(
            self, text="Create an Account", 
            font=("Arial", 32, "bold"), 
            text_color="#2c3e50"
        )
        self.label_title.grid(row=0, column=0, columnspan=2, pady=30)

        # Full Name Field
        self.entry_full_name = ctk.CTkEntry(
            self, placeholder_text="Full Name", 
            width=400, font=("Arial", 16), height=50
        )
        self.entry_full_name.grid(row=1, column=0, columnspan=2, padx=20, pady=15)

        # Email Field
        self.entry_email = ctk.CTkEntry(
            self, placeholder_text="Email", 
            width=400, font=("Arial", 16), height=50
        )
        self.entry_email.grid(row=2, column=0, columnspan=2, padx=20, pady=15)

        # Password Field
        self.entry_password = ctk.CTkEntry(
            self, placeholder_text="Password", 
            show="*", width=400, font=("Arial", 16), height=50
        )
        self.entry_password.grid(row=3, column=0, columnspan=2, padx=20, pady=15)

        # Signup Button
        self.button_signup = ctk.CTkButton(
            self, text="Sign Up", command=self.signup,
            fg_color="#3498db", hover_color="#2980b9", 
            text_color="white", font=("Arial", 18, "bold"), 
            width=200, height=50
        )
        self.button_signup.grid(row=4, column=0, columnspan=2, pady=25)

        # Login Button
        self.button_login = ctk.CTkButton(
            self, text="Already have an account? Login", 
            command=self.show_login,
            fg_color="#ecf0f1", hover_color="#bdc3c7", 
            text_color="#2c3e50", font=("Arial", 14), 
            width=200, height=40
        )
        self.button_login.grid(row=5, column=0, columnspan=2, pady=15)


    def validate_password(self, password):
        """Validates the strength of a password."""
        if len(password) < 8:
            return "Password must be at least 8 characters long."
        if not any(char.isupper() for char in password):
            return "Password must contain at least one uppercase letter."
        if not any(char.islower() for char in password):
            return "Password must contain at least one lowercase letter."
        if not any(char.isdigit() for char in password):
            return "Password must contain at least one number."
        if not any(char in "!@#$%^&*()_+[]{}|;:',.<>?/~`-" for char in password):
            return "Password must contain at least one special character."
        return None

    def signup(self):
        full_name = self.entry_full_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        # Validation: Check if fields are empty
        if not full_name or not email or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        # Validate password strength
        password_error = self.validate_password(password)
        if password_error:
            messagebox.showerror("Password Error", password_error)
            return

        # Proceed with signup
        conn = open_db_connection()
        user_manager = UserManager(conn)
        hashed_password = hash_password(password)
        is_created = user_manager.create_user(full_name, email, hashed_password)
        if is_created["status"] == "ok":
            messagebox.showinfo("Successful Signup", "Account created successfully!")
            self.show_login()  # Redirect to login
        else:
            messagebox.showerror("Signup Error", is_created["message"])
        close_db_connection(conn)

    def show_login(self):
        self.app.show_login_screen()
