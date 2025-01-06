from app import App 
from app.database import init_db


# Start the app
if __name__ == "__main__":
    # Initialize the database
    init_db()
    # Start the app
    app = App()
    app.run()
