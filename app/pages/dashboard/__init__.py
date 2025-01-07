import customtkinter as ctk
from tkinter import messagebox

# class Dashboard(ctk.CTkFrame):
#     def __init__(self, master, app):
#         super().__init__(master)
#         self.app = app

#         # Configure the frame layout
#         self.configure(fg_color="#f2f2f2")
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_rowconfigure(0, weight=1)

#         # Add a welcome message
#         self.label_welcome = ctk.CTkLabel(
#             self, 
#             text=f"Welcome, {self.app.user_session[1]}!", 
#             font=("Arial", 24, "bold"),
#             text_color="#2c3e50"
#         )
#         self.label_welcome.grid(row=0, column=0, pady=20, padx=20)

#         # Add a logout button
#         self.button_logout = ctk.CTkButton(
#             self, text="Logout", command=self.logout,
#             fg_color="#e74c3c", hover_color="#c0392b", 
#             text_color="white", font=("Arial", 16, "bold")
#         )
#         self.button_logout.grid(row=1, column=0, pady=20, padx=20)

#     def logout(self):
#         """Logs the user out and redirects to the login screen."""
#         self.app.clear_user_session()
#         messagebox.showinfo("Logged Out", "You have been logged out, ba bay.")
#         self.app.show_login_screen()





import customtkinter as ctk
from tkinter import Canvas, PhotoImage, messagebox, Tk, Button
from pathlib import Path


def relative_to_assets(path: str) -> Path:
    return Path(__file__).parent / "assets" / Path(path)


class Dashboard(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app

        self.configure(fg_color="#FFFFFF")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Canvas creation
        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=600,
            width=767,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Adding images to the canvas
        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.canvas.create_image(104.0, 300.0, image=image_image_1)

        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.canvas.create_image(106.0, 95.0, image=image_image_2)

        image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        self.canvas.create_image(486.0, 301.0, image=image_image_3)

        # Button definitions (Place them accordingly inside the frame)
        self.create_button("button_1.png", 24.0, 518.0, "button_1 clicked")
        self.create_button("button_2.png", 24.0, 380.0, "button_2 clicked")
        self.create_button("button_3.png", 24.0, 313.0, "button_3 clicked")
        self.create_button("button_4.png", 24.0, 246.0, "button_4 clicked")
        self.create_button("button_5.png", 24.0, 179.0, "button_5 clicked")
        self.create_button("button_6.png", 492.0, 484.0, "button_6 clicked", 255, 90)
        self.create_button("button_7.png", 225.0, 484.0, "button_7 clicked", 255, 90)
        self.create_button("button_8.png", 225.0, 438.0, "button_8 clicked", 522, 37)
        self.create_button("button_9.png", 492.0, 327.0, "button_9 clicked", 255, 90)
        self.create_button("button_10.png", 225.0, 327.0, "button_10 clicked", 255, 90)
        self.create_button("button_11.png", 225.0, 282.0, "button_11 clicked", 522, 37)
        self.create_button("button_12.png", 492.0, 171.0, "button_12 clicked", 255, 90)
        self.create_button("button_13.png", 225.0, 171.0, "button_13 clicked", 255, 90)
        self.create_button("button_14.png", 225.0, 126.0, "button_14 clicked", 522, 37)
        self.create_button("button_15.png", 225.0, 21.0, "button_15 clicked", 522, 81)


    def create_button(self, image_file, x, y, command, width=164.0, height=56.0):
        """Helper method to create buttons with images."""
        button_image = PhotoImage(file=relative_to_assets(image_file))
        button = Button(
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print(command),
            relief="flat"
        )
        button.image = button_image  # Keep reference to prevent GC
        button.place(x=x, y=y, width=width, height=height)

    def subscribe(self):
        """Navigate to subscribe."""
        self.app.show_subscribe_screen()

    def profile(self):
        """Navigate to Profile."""
        self.app.show_profile_screen()

    def players(self):
        """Navigate to players."""
        self.app.show_players_screen()

    def logout(self):
        """Logs the user out and redirects to the login screen."""
        self.app.clear_user_session()
        messagebox.showinfo("Logged Out", "You have been logged out successfully.")
        self.app.show_login_screen()


# class Dashboard(ctk.CTkFrame):
#     def __init__(self, master, app):
#         super().__init__(master)
#         self.app = app
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_rowconfigure(0, weight=1)
#         self.configure(fg_color="#FFFFFF")

#         # Create canvas
#         canvas = Canvas(
#             self,
#             bg="#FFFFFF",
#             bd=0,
#             highlightthickness=0,
#             relief="ridge"
#         )
#         canvas.place(x=0, y=0)

#         # Add images to canvas
#         image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
#         canvas.create_image(104.0, 300.0, image=image_image_1)

#         image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
#         canvas.create_image(106.0, 95.0, image=image_image_2)

#         image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
#         canvas.create_image(486.0, 301.0, image=image_image_3)

#         # Buttons
#         button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
#         button_1 = ctk.CTkButton(
#             self,
#             image=button_image_1,
#             text="",
#             fg_color="transparent", 
#             width=164.0, 
#             height=56.0,
#             command=self.subscribe
#         )
#         button_1.place(x=24.0, y=518.0)

#         button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
#         button_2 = ctk.CTkButton(
#             self,
#             image=button_image_2,
#             text="",
#             fg_color="transparent",
#             width=164.0, 
#             height=56.0,
#             command=self.profile
#         )
#         button_2.place(x=24.0, y=380.0)

#         button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
#         button_3 = ctk.CTkButton(
#             self,
#             image=button_image_3,
#             text="",
#             fg_color="transparent",
#             width=164.0, 
#             height=56.0,
#             command=self.players
#         )
#         button_3.place(x=24.0, y=313.0)

#         button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
#         button_4 = ctk.CTkButton(
#             self,
#             image=button_image_4,
#             text="",
#             fg_color="transparent",
#             width=164.0, 
#             height=56.0,
#             command=self.logout
#         )
#         button_4.place(x=24.0, y=246.0)

#         # Add other buttons as needed with specific commands or behaviors
#         # For example:
#         button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
#         button_5 = ctk.CTkButton(
#             self,
#             image=button_image_5,
#             text="",
#             fg_color="transparent",
#             width=164.0, 
#             height=56.0,
#             command=lambda: print("button_5 clicked")
#         )
#         button_5.place(x=24.0, y=179.0)

#         # Add the rest of the buttons as in your original layout
#         # For other buttons like button_6, button_7, etc., replace `lambda` with their respective actions
#         # Example:
#         button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
#         button_6 = ctk.CTkButton(
#             self,
#             image=button_image_6,
#             text="",
#             fg_color="transparent",
#             width=255.0, 
#             height=90.0,
#             command=lambda: print("button_6 clicked")
#         )
#         button_6.place(x=492.0, y=484.0)

#     def subscribe(self):
#         """Navigate to subscribe."""
#         self.app.show_subscribe_screen()

#     def profile(self):
#         """Navigate to Profile."""
#         self.app.show_profile_screen()

#     def players(self):
#         """Navigate to players."""
#         self.app.show_players_screen()

#     def logout(self):
#         """Logs the user out and redirects to the login screen."""
#         self.app.clear_user_session()
#         messagebox.showinfo("Logged Out", "You have been logged out successfully.")
#         self.app.show_login_screen()  # Redirect to the login screen
