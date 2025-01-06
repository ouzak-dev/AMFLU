from . import sqlite3, insert_data, update_data, delete_data, select_data

# UserManager class
class UserManager:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def create_user(self, full_name: str, email: str, password: str) -> None:
        if select_data(self.conn, "users", where={"email": email})["data"]:
            return {"status": "error", "message": "Email already exists!", "data": None}
        return insert_data(self.conn, "users", {"full_name": full_name, "email": email, "password": password})

    def delete_user(self, email: str) -> None:
        return delete_data(self.conn, "users", {"email": email})

    def update_user(self, email: str, updated_data: dict) -> None:
        return update_data(self.conn, "users", updated_data, {"email": email})

    def get_user(self, email: str) -> list:
        return select_data(self.conn, "users", where={"email": email})
    
    def get_all_users(self) -> list:
        return select_data(self.conn, "users")


# AppManager class
class AppManager:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def create_app(self, name: str, email: str, phone: str, location: str, default: int = 0) -> None:
        if select_data(self.conn, "users", where={"email": email})["data"]:
            return {"status": "error", "message": "Email already exists!", "data": None}
        insert_data(self.conn, "app", {"name": name, "email": email, "phone": phone, "location": location, "default": default})

    def delete_app(self, name: str) -> None:
        delete_data(self.conn, "app", {"name": name})

    def update_app(self, name: str, updated_data: dict) -> None:
        update_data(self.conn, "app", updated_data, {"name": name})

    def get_app(self, name: str) -> list:
        return select_data(self.conn, "app", where={"name": name})

    def get_all_apps(self) -> list:
        return select_data(self.conn, "app")
    