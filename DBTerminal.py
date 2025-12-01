from tkinter import filedialog
from sqlite3 import connect

def open_database_dialog():
    """Open a file dialog to select a SQLite database file and connect to it."""
    file_path = filedialog.askopenfilename(
        title="Open SQLite Database",
        filetypes=[("SQLite Database Files", "*.sqlite;*.db"), ("All Files", "*.*")]
    )
    
    if file_path:
        try:
            connection = connect(file_path)
            print(f"Connected to database: {file_path}")
            return connection, file_path
        except Exception as e:
            print(f"Failed to connect to database: {e}")
            return None
    else:
        print("No file selected.")
        return None
    
db_connection, path = open_database_dialog()
while True:
    command = input(path.split("/")[-1]+"> ")
    if command.lower() in ['exit', 'quit']:
        break
    try:
        cursor = db_connection.cursor()
        cursor.execute(command)
        results = cursor.fetchall()
        for row in results:
            print(row)
        db_connection.commit()
    except Exception as e:
        print(f"Error executing command: {e}")
