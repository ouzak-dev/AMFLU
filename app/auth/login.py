import customtkinter as ctk
from tkinter import messagebox
from app.database import open_db_connection, close_db_connection
from app.database.db_setup import UserManager
from . import verify_password


class Login(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app

        # Configure the frame layout
        self.configure(fg_color="#f2f2f2")  # Light gray background
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(list(range(4)), weight=1)

        # Add a title to the login screen
        self.label_title = ctk.CTkLabel(
            self, text="Welcome Back!", 
            font=("Arial", 32, "bold"), 
            text_color="#2c3e50"
        )
        self.label_title.grid(row=0, column=0, columnspan=2, pady=30)

        # Email Field
        self.entry_email = ctk.CTkEntry(
            self, placeholder_text="Email", 
            width=400, font=("Arial", 16), height=50
        )
        self.entry_email.grid(row=1, column=0, columnspan=2, padx=20, pady=15)

        # Password Field
        self.entry_password = ctk.CTkEntry(
            self, placeholder_text="Password", 
            show="*", width=400, font=("Arial", 16), height=50
        )
        self.entry_password.grid(row=2, column=0, columnspan=2, padx=20, pady=15)

        # Login Button
        self.button_login = ctk.CTkButton(
            self, text="Login", command=self.login,
            fg_color="#3498db", hover_color="#2980b9", 
            text_color="white", font=("Arial", 18, "bold"), 
            width=200, height=50
        )
        self.button_login.grid(row=3, column=0, columnspan=2, pady=25)

        # Signup Button
        self.button_signup = ctk.CTkButton(
            self, text="Don't have an account? Sign Up", 
            command=self.show_signup,
            fg_color="#ecf0f1", hover_color="#bdc3c7", 
            text_color="#2c3e50", font=("Arial", 14), 
            width=200, height=40
        )
        self.button_signup.grid(row=4, column=0, columnspan=2, pady=15)

    def login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        """Handles user login."""
        if not email or not password:
            messagebox.showerror("Error", "Both fields are required!")
            return
        conn = open_db_connection()
        user_manager = UserManager(conn)
        # Validate credentials
        user = user_manager.get_user(email)
        if user['data'] == []:
            messagebox.showerror("Error", "This Email doesn't exist in our database!")
        else:
            if verify_password(user["data"][0][3], password):
                messagebox.showinfo("Success Login", f"Welcome, {user["data"][0][1]}!")
                self.app.set_user_session(user["data"][0])  # Set user session
                self.app.show_dashboard_screen()  # Redirect to the dashboard
            else:
                messagebox.showerror("Login Failed", "Invalid password!")
                return
        close_db_connection(conn)

    def show_signup(self):
        self.app.show_signup_screen()

