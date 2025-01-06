import customtkinter as ctk
from tkinter import messagebox

class Dashboard(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app

        # Configure the frame layout
        self.configure(fg_color="#f2f2f2")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Add a welcome message
        self.label_welcome = ctk.CTkLabel(
            self, 
            text=f"Welcome, {self.app.user_session[1]}!", 
            font=("Arial", 24, "bold"),
            text_color="#2c3e50"
        )
        self.label_welcome.grid(row=0, column=0, pady=20, padx=20)

        # Add a logout button
        self.button_logout = ctk.CTkButton(
            self, text="Logout", command=self.logout,
            fg_color="#e74c3c", hover_color="#c0392b", 
            text_color="white", font=("Arial", 16, "bold")
        )
        self.button_logout.grid(row=1, column=0, pady=20, padx=20)

    def logout(self):
        """Logs the user out and redirects to the login screen."""
        self.app.clear_user_session()
        messagebox.showinfo("Logged Out", "You have been logged out, ba bay.")
        self.app.show_login_screen()
