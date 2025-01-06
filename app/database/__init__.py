import sqlite3


# Function to create tables in the database
def create_tables(conn: sqlite3.Connection, table_name: str, columns: tuple) -> bool:
    try:
        cursor = conn.cursor()
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} {str(columns).replace("'", "")}""")
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(e)
        return False


# Function to check if a table exists
def table_exists(conn: sqlite3.Connection, table_name: str) -> bool:
    # Create a cursor object
    cursor = conn.cursor()
    # Query sqlite_master to check if the table exists
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?",(table_name,))
    result = cursor.fetchone()
    return result is not None


# Function to update data in a table
def update_data(conn: sqlite3.Connection, table_name: str, updated_data: dict, where: dict = None) -> None:
    try:
        cursor = conn.cursor()
        update_keys = ", ".join(f"{key} = ?" for key in updated_data)
        data = tuple(updated_data.values())
        if where:
            where_keys = " AND ".join(f"{key} = ?" for key in where)
            where_values = tuple(where.values())
            query = f"UPDATE {table_name} SET {update_keys} WHERE {where_keys}"
            data += where_values
        else:
            query = f"UPDATE {table_name} SET {update_keys}"
        cursor.execute(query, data)
        conn.commit()
        print(f"Updated {cursor.rowcount} rows in table '{table_name}'.")
        return {"status": "ok", "message": f"Updated Successfuly.", "data": cursor.fetchone()}
    except sqlite3.IntegrityError as e:
        return {"status": "error", "message": e, "data": None}

# Function to insert data into a table
def insert_data(conn: sqlite3.Connection, table_name: str, data: dict) -> None:
    try:
        cursor = conn.cursor()
        columns = ", ".join(data.keys())
        placeholders = ", ".join("?" for _ in data)
        values = tuple(data.values())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(query, values)
        conn.commit()
        print(f"Inserted data into table '{table_name}'.")
        return {"status": "ok", "message": f"Inserted Successfuly.", "data": cursor.fetchone()}
    except sqlite3.IntegrityError as e:
        return {"status": "error", "message": e, "data": None}


# Function to delete data from a table
def delete_data(conn: sqlite3.Connection, table_name: str, where: dict = None) -> None:
    try:
        cursor = conn.cursor()
        if where:
            where_keys = " AND ".join(f"{key} = ?" for key in where)
            where_values = tuple(where.values())
            query = f"DELETE FROM {table_name} WHERE {where_keys}"
            cursor.execute(query, where_values)
        else:
            query = f"DELETE FROM {table_name}"
            cursor.execute(query)
        conn.commit()
        print(f"Deleted {cursor.rowcount} rows from table '{table_name}'.")
        return {"status": "ok", "message": f"Deleted Successfully.", "data": None}
    except sqlite3.IntegrityError as e:
        return {"status": "error", "message": e, "data": None}


# Function to select data from a table with additional options
def select_data(conn: sqlite3.Connection, table_name: str, columns: list = None, where: dict = None, distinct: bool = False, 
                order_by: str = None, limit: int = None) -> list:
    cursor = conn.cursor()
    # Build SELECT clause
    columns_part = ", ".join(columns) if columns else "*"
    distinct_clause = "DISTINCT " if distinct else ""
    # Build WHERE clause
    if where:
        where_keys = " AND ".join(f"{key} = ?" for key in where)
        where_values = tuple(where.values())
        where_clause = f"WHERE {where_keys}"
    else:
        where_clause = ""
        where_values = ()
    # Build ORDER BY and LIMIT clauses
    order_by_clause = f"ORDER BY {order_by}" if order_by else ""
    limit_clause = f"LIMIT {limit}" if limit else ""
    # Combine the query
    query = f"""SELECT {distinct_clause}{columns_part} FROM {table_name} {where_clause} {order_by_clause} {limit_clause}""".strip()
    cursor.execute(query, where_values)
    data = cursor.fetchall()
    return {"status": "ok", "message": f"{len(data)} rows fitched.", "data": data}


def open_db_connection() -> sqlite3.Connection:
    """Returns a connection to the SQLite database."""
    return sqlite3.connect("database.db")


def close_db_connection(conn: sqlite3.Connection) -> None:
    """Closes the connection to the SQLite database."""
    conn.close()


# initialize the database
def init_db():
    """Initializes the database with the required schema."""
    conn = open_db_connection()
    if not table_exists(conn, "users"):
        if create_tables(conn, "users", ('id INTEGER PRIMARY KEY AUTOINCREMENT', 'full_name TEXT NOT NULL', 'email TEXT UNIQUE NOT NULL', 'password TEXT NOT NULL')):
            insert_data(conn, "users", {"full_name": "AMFLU Admin", "email": "contact@amflu.com", "password": "0e89f223e226ae63268cf39152ab75722e811b89d29efb22a852f1667bd22ae0"}) # password: admin2025
        else:
            pass
    elif not table_exists(conn, "app"):
        if create_tables(conn, "app", ('id INTEGER PRIMARY KEY AUTOINCREMENT', 'name TEXT UNIQUE NOT NULL', 'email TEXT NOT NULL', 'phone TEXT NOT NULL', 'location TEXT NOT NULL', 'default INTEGER NOT NULL DEFAULT 1')):
            insert_data(conn, "app", {"name": "AMFLU", "email": "contact@amflu.com", "phone": "+212(6)4842-4326", "location": "123 Main St, New York, NY, 10001", "default": 1},)
        else:
            pass
    else:
        pass
    conn.commit()
    close_db_connection(conn)
    print("Database initialized successfully.")
