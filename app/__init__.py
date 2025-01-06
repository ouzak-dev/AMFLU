import tkinter as tk
import customtkinter as ctk
from app.auth.login import Login
from app.auth.signup import Signup
from app.pages.dashboard import Dashboard


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Stores the logged-in user's session
        self.user_session = None  

        # Application title
        self.title("My Desktop Application")

        # Make the freem zoomed
        # self.wm_attributes('-zoomed', True)
        self.geometry("1080x900")
        
        # Configure grid layout for centering
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        # Initial screen setup
        self.show_login_screen()

    def set_user_session(self, user):
        """Sets the current user session."""
        self.user_session = user

    def clear_user_session(self):
        """Clears the current user session."""
        self.user_session = None

    def show_dashboard_screen(self):
        """Displays the main dashboard."""
        self.clear_frames()
        
        # Configure grid layout for centering
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Create a frame to hold the content and center it
        content_frame = ctk.CTkFrame(self)
        content_frame.grid(row=0, column=0, sticky="nsew")
        
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
        
        self.dashboard_screen = Dashboard(content_frame, self)
        self.dashboard_screen.grid(row=0, column=0, padx=20, pady=20)  # Adjust padding for compactness

    def show_login_screen(self):
        """Displays the login screen."""
        self.clear_frames()
        
        # Configure grid layout for centering
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Create a frame to hold the content and center it
        content_frame = ctk.CTkFrame(self)
        content_frame.grid(row=0, column=0, sticky="nsew")
        
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
        
        self.login_screen = Login(content_frame, self)
        self.login_screen.grid(row=0, column=0, padx=20, pady=20)  # Adjust padding for compactness

    def show_signup_screen(self):
        """Displays the signup screen."""
        self.clear_frames()
        
        # Configure grid layout for centering
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Create a frame to hold the content and center it
        content_frame = ctk.CTkFrame(self)
        content_frame.grid(row=0, column=0, sticky="nsew")
        
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
        
        self.signup_screen = Signup(content_frame, self)
        self.signup_screen.grid(row=0, column=0, padx=20, pady=20)  # Adjust padding for compactness

    def clear_frames(self):
        """Clears all frames to switch screens."""
        for widget in self.winfo_children():
            widget.destroy()

    def run(self):
        self.mainloop()

